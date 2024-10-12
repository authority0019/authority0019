from scapy.all import *
import pandas as pd
from sklearn.ensemble import IsolationForest
import sqlite3
import logging

# Set up logging
logging.basicConfig(filename='traffic_analyzer.log', level=logging.INFO)

# Initialize database connection
conn = sqlite3.connect('traffic_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS traffic (timestamp TEXT, ip_src TEXT, ip_dst TEXT, protocol TEXT)''')

# Initialize packet data storage
packet_data = []

def packet_handler(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        # Store packet data for analysis
        packet_data.append((str(pd.Timestamp.now()), ip_src, ip_dst, protocol))
        
        # Perform analysis every 100 packets
        if len(packet_data) >= 100:
            analyze_packets()

def analyze_packets():
    global packet_data
    
    df = pd.DataFrame(packet_data, columns=['timestamp', 'ip_src', 'ip_dst', 'protocol'])
    
    # Convert categorical data to numerical data
    df['protocol'] = df['protocol'].astype('category').cat.codes
    
    # Train Isolation Forest model for anomaly detection
    model = IsolationForest(contamination=0.1)
    model.fit(df[['protocol']])
    
    # Predict anomalies
    predictions = model.predict(df[['protocol']])
    
    # Log anomalies
    for index, pred in enumerate(predictions):
        if pred == -1:
            logging.warning(f"Anomaly detected from {df.iloc[index]['ip_src']} to {df.iloc[index]['ip_dst']}")
            c.execute("INSERT INTO traffic VALUES (?, ?, ?, ?)", (str(pd.Timestamp.now()), df.iloc[index]['ip_src'], df.iloc[index]['ip_dst'], str(df.iloc[index]['protocol'])))
    
    conn.commit()
    packet_data.clear()  # Clear data after analysis

# Start capturing packets
print("Starting Advanced Network Traffic Analyzer...")
sniff(prn=packet_handler, store=0)