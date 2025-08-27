import streamlit as st
import time
import datetime
import requests
from PIL import Image

# --- Page Configuration ---
st.set_page_config(
    page_title="FlipXForecast",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Professional Dark Theme Styling ---
st.markdown("""
<style>
    /* Main App Styling - Professional Dark Theme */
    .stApp {
        background-color: #0E1117; /* GitHub Dark Background */
        color: #C9D1D9; /* GitHub Dark Text */
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #161B22; /* GitHub Dark Paper Background */
        border-right: 1px solid #30363D;
    }

    /* Title and Header Styling */
    h1, h2, h3 {
        color: #58A6FF; /* GitHub Dark Link Blue for Headers */
    }
    
    /* Radio Button Styling */
    .st-emotion-cache-1y4p8pa {
        background-color: #0D1117;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 10px;
    }

    /* Button Styling */
    .stButton>button {
        color: #FFFFFF;
        background-color: #238636; /* GitHub Green */
        border-radius: 8px;
        border: 1px solid #30363D;
        padding: 10px 24px;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #2EA043;
        border-color: #8B949E;
        transform: scale(1.02);
    }
    .stButton>button:disabled {
        background-color: #21262D;
        color: #8B949E;
        border-color: #30363D;
    }

    /* Metric Styling */
    .stMetric {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .stMetric > div > div > .st-emotion-cache-1xarl3l {
        font-size: 2.5rem;
        color: #58A6FF; /* GitHub Blue for Metric Value */
    }
    .stMetric > label {
        color: #8B949E; /* GitHub Secondary Text */
    }

    /* Info/Alert Box Styling */
    .stAlert {
        border-radius: 8px;
        background-color: #161B22;
        border: 1px solid #30363D;
    }

    /* Text Input */
    .stTextInput > div > div > input {
        background-color: #0D1117;
        color: #C9D1D9;
        border: 1px solid #30363D;
        border-radius: 8px;
    }

    /* Footer Styling - Revamped */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #161B22;
        color: #8B949E;
        padding: 15px 0;
        font-size: 14px;
        border-top: 1px solid #30363D;
    }
    .footer-content {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 15px;
    }
    .footer a {
        color: #58A6FF; /* GitHub Blue for links */
        text-decoration: none;
        transition: color 0.3s;
    }
    .footer a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)


# --- State Management ---
if 'stopwatch_start_time' not in st.session_state:
    st.session_state.stopwatch_start_time = 0
if 'stopwatch_elapsed_time' not in st.session_state:
    st.session_state.stopwatch_elapsed_time = 0
if 'stopwatch_running' not in st.session_state:
    st.session_state.stopwatch_running = False

if 'timer_start_time' not in st.session_state:
    st.session_state.timer_start_time = 0
if 'timer_duration' not in st.session_state:
    st.session_state.timer_duration = 0
if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False

# --- Feature Functions ---

def alarm_clock():
    st.header("⏰ Alarm Clock")
    st.info("Set a time and get a notification. A simple and elegant alarm clock.")
    
    alarm_time = st.time_input("Set an alarm for:", datetime.time(8, 30))
    st.write(f"Your alarm is currently set for **{alarm_time.strftime('%I:%M %p')}**")
    
    if st.button("Set Alarm"):
        st.success(f"Success! Alarm has been set for {alarm_time.strftime('%I:%M %p')}!")

def stopwatch():
    st.header("⏱️ Stopwatch")

    if st.session_state.stopwatch_running:
        st.session_state.stopwatch_elapsed_time = time.time() - st.session_state.stopwatch_start_time
    
    st.metric(label="Elapsed Time", value=f"{st.session_state.stopwatch_elapsed_time:.2f} s")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start", disabled=st.session_state.stopwatch_running, use_container_width=True):
            st.session_state.stopwatch_start_time = time.time() - st.session_state.stopwatch_elapsed_time
            st.session_state.stopwatch_running = True
            st.rerun()
    with col2:
        if st.button("Stop", disabled=not st.session_state.stopwatch_running, use_container_width=True):
            st.session_state.stopwatch_running = False
            st.rerun()
    with col3:
        if st.button("Reset", use_container_width=True):
            st.session_state.stopwatch_start_time = 0
            st.session_state.stopwatch_elapsed_time = 0
            st.session_state.stopwatch_running = False
            st.rerun()
    
    if st.session_state.stopwatch_running:
        time.sleep(0.01)
        st.rerun()

def timer():
    st.header("⏳ Timer")

    duration_minutes = st.number_input("Set timer duration (minutes):", min_value=0, value=5, step=1)
    
    if st.button("Start Timer", disabled=st.session_state.timer_running):
        st.session_state.timer_duration = duration_minutes * 60
        st.session_state.timer_start_time = time.time()
        st.session_state.timer_running = True
        st.rerun()

    if st.session_state.timer_running:
        elapsed = time.time() - st.session_state.timer_start_time
        remaining = st.session_state.timer_duration - elapsed

        if remaining > 0:
            mins, secs = divmod(int(remaining), 60)
            st.metric(label="Time Remaining", value=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
            st.rerun()
        else:
            st.success("Timer finished!")
            st.balloons()
            st.session_state.timer_running = False

def weather():
    st.header("☀️ Weather of the Day")
    
    API_KEY = st.secrets.get("OPENWEATHERMAP_API_KEY")
    if not API_KEY:
        st.error("Weather API key not found. Please add it to your secrets file.")
        return

    city = st.text_input("Enter a city name:", "London")
    
    if st.button("Get Weather"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            with st.spinner(f"Fetching weather for {city}..."):
                response = requests.get(url)
                data = response.json()

            if data["cod"] == 200:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Temperature", f"{data['main']['temp']} °C")
                with col2:
                    st.metric("Humidity", f"{data['main']['humidity']} %")
                
                st.write(f"**Weather:** {data['weather'][0]['description'].capitalize()}")
                st.write(f"**Wind Speed:** {data['wind']['speed']} m/s")
            else:
                st.error(f"Could not retrieve weather for {city}. Error: {data.get('message', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

# --- Sidebar and Main App Logic ---

with st.sidebar:
    st.title("FlipXForecast")
    st.markdown("---")
    st.header("Select a Tool")
    # Changed the radio button labels to be more intuitive
    selected_tool = st.radio(
        "Select a tool to display:",
        ('Alarm Clock', 'Stopwatch', 'Timer', 'Weather'),
        label_visibility="collapsed"
    )

# --- Main Page Content ---
main_container = st.container()

with main_container:
    # Adjusted column layout to make the logo larger
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        try:
            image = Image.open('logo-png.png')
            # Corrected the deprecated parameter to use_container_width
            st.image(image, use_container_width=True) 
        except FileNotFoundError:
            st.error("logo-png.jpg not found. Please add it to the project folder.")

    st.title("FlipXForecast")
    st.subheader("Unlock Time and Weather in a Twist!")
    st.write("---")

    # Updated the logic to match the new radio button labels
    if selected_tool == 'Alarm Clock':
        alarm_clock()
    elif selected_tool == 'Stopwatch':
        stopwatch()
    elif selected_tool == 'Timer':
        timer()
    elif selected_tool == 'Weather':
        weather()

# --- Footer ---
st.markdown("""
<div class="footer">
    <div class="footer-content">
        <span>Developed by Gopisetty Sai Charan</span>
        <span>|</span>
        <a href="mailto:saicharangopisetty23@gmail.com">saicharangopisetty23@gmail.com</a>
        <span>|</span>
        <span>Phone: +91 9502996405</span>
        <span>|</span>
        <a href="https://www.linkedin.com/in/saicharangopisetty" target="_blank">LinkedIn</a>
    </div>
</div>
""", unsafe_allow_html=True)
