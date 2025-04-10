import time
import os
import sys
import json
import pyautogui
from pynput.mouse import Controller, Button

mouse = Controller()

def resource_path(relative_path):
    """Gets the correct resource path, working for both development and packaged execution."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def click(x, y):
    """Moves the cursor to position (x, y) and simulates a left mouse click."""
    mouse.position = (x, y)
    time.sleep(0.05)
    mouse.click(Button.left, 1)

def wait(seconds):
    time.sleep(seconds)

def load_steps():
    """Loads the JSON file containing the sequence of steps."""
    steps_path = resource_path("steps.json")
    try:
        with open(steps_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File 'steps.json' not found at {steps_path}.")
        return []
    except json.JSONDecodeError:
        print(f"Error parsing JSON from {steps_path}.")
        return []

# Load steps from JSON file
steps = load_steps()

# Dictionary containing coordinates for each button or element
coords = {
    "call_button": (360, 395),
    "call_button_secondary": (361, 431),
    "end_call": (1586, 680),
    "onlysales_icon": (981, 106),
    "onlysales_send": (876, 480),
    "nc_default": (1142, 283)
}

# === MAIN LOOP === #
try:
    while True:
        for index, step in enumerate(steps):
            print(f"Executing step {index + 1}: {step.get('description', 'Running')}")

            if step["action"] == "search_and_click":
                target_key = step["target"].split('.')[0]
                target_coords = coords.get(target_key)
                if target_coords:
                    click(*target_coords)
                    wait(1)
                else:
                    print(f"No coordinates found for '{target_key}'.")

            elif step["action"] == "wait":
                wait(step.get("duration", 1))

            else:
                print(f"Unknown action: {step['action']}")

except KeyboardInterrupt:
    print("\n🛑 Program stopped.")
