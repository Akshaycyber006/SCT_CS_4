# SCT_CS_4

# Basic Keylogger
A simple educational keylogger program that records and logs keystrokes to a file. This tool demonstrates fundamental keystroke logging concepts for learning purposes only.

# ⚠️ Important Disclaimer
This keylogger is intended for educational purposes only.

Unauthorized use of keyloggers is illegal and unethical in most jurisdictions
Only use on systems you own or have explicit permission to monitor
The creator assumes no responsibility for misuse of this software
Always comply with applicable laws and regulations regarding privacy and surveillance
Description
This basic keylogger captures both regular character keys and special keys (like Shift, Enter, etc.), timestamps each keystroke, and saves the logs to a text file. It's designed to help understand how keystroke logging works at a fundamental level.

# Installation
Clone this repository:
bash
cd basic-keylogger
pip install pynput
SAVE AS
python keylogger.py

Type on your keyboard - all keystrokes will be recorded.
Press ESC to stop the keylogger.
Check the keylog.txt file for the recorded keystrokes.
Features
Records both regular character keys and special keys
Timestamps each keystroke with date and time
Saves logs to a text file in the same directory
Stops gracefully when ESC key is pressed
Shows the full path to the log file when stopped
Sample Log Output

Line Wrapping
# Ex OUTPUT
Keylogger started at 2023-11-15 14:30:00
--------------------------------------------------
2023-11-15 14:30:05 - Key pressed: h
2023-11-15 14:30:05 - Key pressed: e
2023-11-15 14:30:06 - Key pressed: l
2023-11-15 14:30:06 - Key pressed: l
2023-11-15 14:30:07 - Key pressed: o
2023-11-15 14:30:08 - Special key: Key.space
2023-11-15 14:30:09 - Key pressed: w
2023-11-15 14:30:09 - Key pressed: o
2023-11-15 14:30:10 - Key pressed: r
2023-11-15 14:30:10 - Key pressed: l
2023-11-15 14:30:11 - Key pressed: d
2023-11-15 14:30:12 - Special key: Key.enter
# Important Notes
Antivirus Software: Many antivirus programs will flag keyloggers as potentially malicious software.
System Permissions: On some systems (especially macOS and Linux), you may need to grant accessibility permissions for the program to work.
Transparency: Always inform users if their keystrokes are being logged on systems you own.
Security: This program saves logs in plain text format, which is not secure for sensitive information.
# How It Works
Uses the pynput library to monitor keyboard events
The on_press function captures each key press
Regular keys are logged as characters
Special keys (like Shift, Enter, etc.) are logged by their key name
Each entry includes a timestamp
The on_release function stops the logger when ESC is pressed
All entries are saved to a text file
Ethical Considerations
# This tool should only be used for:

Educational purposes to understand cybersecurity concepts
Testing your own systems with explicit permission
Research with proper authorization
# Never use this tool to:

Monitor others without their knowledge and consent
Capture sensitive information like passwords or financial data
Violate privacy laws or terms of service
