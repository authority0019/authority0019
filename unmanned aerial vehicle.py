from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import numpy as np
import cv2

# Connect to unmanned aerial vehicle
vehicle = connect('udp:127.0.0.1:14551', wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def fly_to(location):
    print(f"Flying to {location}")
    vehicle.simple_goto(location)

def waypoint_mission(waypoints):
    for point in waypoints:
        fly_to(point)
        time.sleep(30)  # Wait 30 seconds per point

def return_to_launch():
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")

def obstacle_avoidance():
    # Avoiding objects
    cap = cv2.VideoCapture(0)  # Opening the camera

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Viewing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)

        # Detect possible objects
        if np.sum(edges) > 100000:  # If detected:
            print("Obstacle detected! Changing course.")
            vehicle.mode = VehicleMode("LOITER")  # Switch to waiting mode
            time.sleep(5)  # Wait 5 seconds
            continue
        
        cv2.imshow('Obstacle Detection', edges)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# The main code
if __name__ == "__main__":
    try:
        arm_and_takeoff(10)  # 10 meter takeoff
        
        # Waypoints
        waypoints = [
            LocationGlobalRelative(37.7749, -122.4194, 10),  # Dot 1
            LocationGlobalRelative(37.7750, -122.4184, 10),  # Dot 2
            LocationGlobalRelative(37.7751, -122.4170, 10),  # Dot 3
            LocationGlobalRelative(37.7752, -122.4160, 10)   # Dot 4
        ]

        # Obstacle avoidance
        obstacle_avoidance()

        waypoint_mission(waypoints)  # Start Waypoint

        # Before landing
        return_to_launch()

    finally:
        # Closing the unmanned aerial vehicle
        vehicle.close()


        #pip install dronekit numpy opencv-python before running the code
