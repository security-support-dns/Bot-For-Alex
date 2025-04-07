import pyautogui
import time
import json

pyautogui.FAILSAFE = True

# 🔴 Configurable delay between actions
ACTION_DELAY = 0.5

def detect_cursor_position():
    """Detect and log the current cursor position."""
    pos = pyautogui.position()
    print(f"📍 Current cursor position detected: ({pos.x}, {pos.y})")

def validate_step(step, required_keys):
    """Validate that the step contains all required keys."""
    for key in required_keys:
        if key not in step:
            print(f"⚠️ Skipping step: Missing required key '{key}' in step: {step}")
            return False
    return True

def run_automation(steps):
    print("🚦 Running automation in 3 seconds...")
    time.sleep(3)
    detect_cursor_position()  # Detect cursor position before starting automation
    try:
        for i, step in enumerate(steps):
            if step["action"] == "click":
                if not validate_step(step, ["x", "y", "button"]):
                    continue
                pyautogui.moveTo(step["x"], step["y"], duration=0.5)
                pyautogui.click(button=step.get("button", "left"))
                print(f"🖱️ Step {i+1}: {step['button'].capitalize()} click at ({step['x']}, {step['y']})")
            elif step["action"] == "move":
                if not validate_step(step, ["x", "y"]):
                    continue
                pyautogui.moveTo(step["x"], step["y"], duration=0.5)
                print(f"➡️ Step {i+1}: Moved to ({step['x']}, {step['y']})")
            elif step["action"] == "drag":
                if not validate_step(step, ["startX", "startY", "endX", "endY"]):
                    continue
                pyautogui.moveTo(step["startX"], step["startY"], duration=0.5)
                pyautogui.dragTo(step["endX"], step["endY"], duration=0.5, button="left")
                print(f"🖱️ Step {i+1}: Dragged from ({step['startX']}, {step['startY']}) to ({step['endX']}, {step['endY']})")
            else:
                print(f"⚠️ Step {i+1}: Unknown action '{step['action']}'")
            time.sleep(ACTION_DELAY)
        print("✅ Automation complete!")
    except Exception as e:
        print(f"❌ Error during automation: {e}")

def main():
    try:
        with open("automation_steps.json", "r") as f:
            steps = json.load(f)
        print("📂 Steps loaded from `automation_steps.json`")
        run_automation(steps)
    except FileNotFoundError:
        print("⚠️ File `automation_steps.json` not found. Please create it with valid steps.")
    except Exception as e:
        print(f"❌ Error: {e}")

# Automatically start the automation process
if __name__ == "__main__":
    main()