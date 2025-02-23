import os
import time
import streamlit as st

FIRE_TV_IP = "192.168.1.3"  # Replace with your Fire TV Stick’s IP

def is_fire_tv_online():
    """Checks if Fire TV is online using ADB."""
    response = os.popen(f"adb connect {FIRE_TV_IP}").read()
    return "connected" in response or "already connected" in response

def press_key(key, delay=1):
    """Press a key and wait."""
    os.system(f"adb shell input keyevent {key}")
    time.sleep(delay)

def tap_coordinates(x, y, delay=1):
    """Tap on specific screen coordinates."""
    os.system(f"adb shell input tap {x} {y}")
    time.sleep(delay)

def automation_sequence():
    st.write("Waiting for Fire TV Stick to turn on...")
    while not is_fire_tv_online():
        time.sleep(5)

    st.write("Fire TV is online. Starting sequence...")
    press_key(3)  # Home button
    time.sleep(7)

    st.write("Moving right 5 times...")
    for _ in range(5):
        press_key(22, delay=0.5)  # Right arrow

    st.write("Pressing OK button...")
    press_key(23)
    time.sleep(8)

    st.write("Tapping at coordinates (135, 1500)...")
    tap_coordinates(135, 1500)
    time.sleep(5)

    st.write("Pressing and holding Home button for 5 seconds...")
    os.system("adb shell input keyevent --longpress 3")
    time.sleep(5)

    time.sleep(4)
    st.write("Pressing Return button...")
    press_key(4)

    st.success("Automation complete!")

# Streamlit UI
st.title("Fire TV Automation")
st.write("Click the button below to start the automation sequence.")

if st.button("Run Automation"):
    automation_sequence()
