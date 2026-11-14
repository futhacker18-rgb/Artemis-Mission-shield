import streamlit as st
from datetime import datetime
import pandas as pd
import requests

st.set_page_config(
    page_title="Artemis Mission shield",
    page_icon="🚀",
    layout="wide"
)
st.markdown("""

<style>
[data-testid="stAppViewContainer"]{
    background-color: #060913;
    background-image:
        radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 3px),
        radial-gradient(#00d4ff, rgba(0,212,255,.15) 1px,transparent 2px),
        radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 3px);
    background-size: 350px 350px, 250px 250px, 150px 150px;
    background-position: 0 0, 40px 60px, 130px 270px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Artemis Mission Shield")

st.subheader("Lunar Outpost Mission Control")

st.write(
    "Welcome, Commander! "
    "your mission is to manage the lunar outpost "
    "and protect its systems."
)

st.subheader("📡 Live NASA Deep-space Threat Feed")
try:
    res = requests.get("https://nasa.gov",timeout=5).json()
    today_key = list(res["near_earth_objects"].keys())[0]
    neo = res["near_earth_objects"][today_key][0]
    speed = float(neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])
    st.warning(f"⚠️ Live NASA NEO Aleart: Tracking real object **{neo['name']}** moving at **{speed:,.0f} km/h**!")
except Exception:
    st.warning("⚠️ Live NASA NEO Telemetry: Tracking Near-Earth Asteroid **(2026 AB1)** at **48,320 km/h** | Shielding Nominal")

st.divider()

st.header("Mission Status")

col1, col2, col3 = st.columns(3)

col1.metric("Oxygen Level","95%","Stable")
col2.metric("Power Level","85%","Normal")
col3.metric("Food Supply","95%","Stable")

st.divider()

st.info(
    "Mission systems are initializing."
    "Welcome aboard, Commander!"
)
st.subheader("🌙 Resource Monitoring")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Oxygen")
    st.progress(0.95)

with col2:
    st.write("Power")
    st.progress(0.85)

with col3:
    st.write("Food")
    st.progress(0.95)

st.divider()

st.subheader("🛰️ Mission Status")

mission_status = "ACTIVE"

if mission_status == "ACTIVE":
    st.success("Mission is running normally!")
else:
    st.warning("Mission needs attention!")

st.write("Commander,all systems are being monitored.")

st.divider()

st.header("🔐 Cybersecurity Monitoring Center")

st.subheader("Security Alerts")

st.warning("⚠️ Unusual Login Attempt Detected")

st.info("📡Communication Signal Check: Normal")

st.success("🛡️ System Integrity: Protected")

st.divider()

st.subheader("🔍 Run Security Check")

if st.button("Start Security Scan"):

    st.success("Security Scan Completed!)")

    st.write("✅ Login Activity: Normal")
    st.write("✅ Communication: Secure")
    st.write("✅ System Inegrity: Protected")

    st.info("Mission systems are currently safe.")

st.divider()

st.header("🌙 Mission Challenge")

st.write("A sudden power drop has been detected!")

st.subheader("Choose your action")

action = st.selectbox("What should the Commander do?",
                      [
                          "Select an action",
                          "Activate Backup Power",
                          "Ignore the Warning"
                      ]
)

if action == "Activate Backup Power":
    st.success("Backup Power Activated!")
    st.write("Mission Power supply is recovering.")

elif action == "Ignore the Warning":
    st.error("Warning! Power level may become critical.")

else:
    st.info("Waiting for Commander's decision.")

st.divider()

st.header("🌙 Resource Control Simulator")

oxygen = st.slider("Oxygen Supply", 0, 100, 95)
power = st.slider("Power Supply", 0, 100, 85)
food = st.slider("Food Supply", 0, 100, 95)

st.subheader("Current Resource Levels")

col1, col2, col3 = st.columns(3)

col1.metric("Oxygen", f"{oxygen}%")
col2.metric("Power", f"{power}%")
col3.metric("Food", f"{food}%")

if oxygen < 30 or power < 30 or food < 30:
    st.warning("Resource level critical! Take action.")

else:
    st.success("All Resources are at safe levels.")

st.divider()

st.header("🚨 Advanced Mission Monitering")

st.subheader("Resource Alerts")

if oxygen < 30:
    st.error("Oxygen level critical!")

if power < 30:
    st.error("Power level critical!")

if food < 30:
    st.error("Food supply critical!")

if oxygen >= 30 and power >= 30 and food >= 30:
    st.success("All resources are stable!")

st.divider()

st.subheader("☢️ Radiation Monitoring")

radiation = st.slider(
    "Radiation Level",
    0, 100, 20
)

if radiation >= 70:
    st.error("High Radiation Alert! Review shelter protection.")

elif radiation >= 40:
    st.warning("Radiation Level elevated. Monitor closely.")

else:
    st.success("Radiation level is within safe simulation range.")

st.divider()

st.header("📡 Communication Monitoring")

communication = st.slider(
    "Communication Signal",
    0,100,90
)
if communication >= 70:
    st.success("Communication Signal: Strong")

elif communication >= 40:
    st.warning("Communication Signal: Weak")

else:
    st.error("Communication Failure! Check the signal.")

st.divider()

st.header("🏆 Mission Performance Score")

mission_score = int(
    (oxygen + power + food + communication + (100-radiation))/5
)

st.metric("Mission Score", f"{mission_score}/100")

if mission_score >= 80:
    st.success("Excellent Mission Performance!")

elif mission_score >=50:
    st.warning("Mission Performance: Needs improvement")

else:
    st.error("Mission Performance: Critical")

st.divider()

st.header("🔐 Cybersecurity Event log")

if "security_events" not in st.session_state:
    st.session_state.security_events = []

event = st.selectbox(
    "Select Security Event",
    [
        "Unusual Login Attempt",
        "Communication Signal Issue",
        "System Integrity Check"
    ]
)

if st.button("Record Security event"):
    st.session_state.security_events.append(
        f"{datetime.now().strftime('%H:%M:%S')}-{event}"
    )
    st.success("Security event recorded!")

st.subheader("Recent Security Events")

for item in reversed(st.session_state.security_events[-5:]):
    st.write("🔹",item)

if st.session_state.security_events:
    events_df = pd.DataFrame(
        st.session_state.security_events,
        columns=["Security Event"]
    )

    events_csv = events_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Security Events",
        data=events_csv,
        file_name="Security_events.csv",
        mime="text/csv"
    )
else:
    st.info("No security events recorded yet.")

st.divider()

st.header("📋 Mission History")

if "mission_history" not in st.session_state:
    st.session_state.mission_history = []

if st.button("Save Mission Snapshot"):
    st.session_state.mission_history.append(
    {
        "time":datetime.now().strftime("%H:%M:%S"),
        "oxygen":oxygen,
        "power":power,
        "food":food,
        "radiation":radiation,
        "score":mission_score
    }
)

    st.success("Mission snapshot saved!")

for record in reversed(st.session_state.mission_history[-5:]):
    st.write(
        f"🕒{record['time']} |"
        f"Oxygen: {record['oxygen']}% |"
        f"Power: {record['power']}% |"
        f"Food: {record['food']}% |"
        f"Radiation: {record['radiation']}% |"
        f"Score: {record['score']}/100"
    )

if st.session_state.mission_history:
    history_df = pd.DataFrame(st.session_state.mission_history)

    csv_data = history_df.to_csv(index=False)

    st.download_button(
        label="📥 Download Mission History",
        data=csv_data,
        file_name="mission_history.csv",
        mime="text/csv"
    )
else:
    st.info("No mission history available yet.")
