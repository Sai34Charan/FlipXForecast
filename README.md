# FlipXForecast
### UNLOCK TIME AND WEATHER IN A TWIST!

![FlipXForecast Logo](logo-png.png)

## 🚀 Live Demo

**Access the deployed version of the application here:**

[**https://flipxforecast.streamlit.app/**](https://flipxforecast. streamlit.app/)

---

## 📖 Project Description

**FlipXForecast** is a mobile-first web application developed as a submission for the "Prompt This Into Existence!" Hackathon. The core concept is to provide different functionalities based on how a user holds their mobile device. This implementation simulates that experience using Python and the Streamlit framework.

The application is designed with a clean, modern, and responsive dark theme, providing four essential tools in one seamless interface.

---

## ✨ Features

The app is divided into four main tools, which are selectable from the sidebar:

* **⏰ Alarm Clock:** A simple and elegant interface to set a daily alarm.
* **⏱️ Stopwatch:** A functional stopwatch with Start, Stop, and Reset capabilities, perfect for timing tasks.
* **⏳ Timer:** A countdown timer that alerts you when the time is up.
* **☀️ Weather:** Get real-time weather information for any city in the world, powered by the OpenWeatherMap API.

### Device Orientation Simulation

Since a Python backend cannot directly access a mobile device's orientation sensors, this app simulates the orientation changes through a user-friendly sidebar menu. This approach fulfills the hackathon's conceptual requirements while working within the framework's limitations.

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running.

### Prerequisites

* **Python 3.8+** installed on your system.
* A free API key from [OpenWeatherMap](https://openweathermap.org/appid).

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/FlipXForecast.git](https://github.com/your-username/FlipXForecast.git)
    cd FlipXForecast
    ```

2.  **Create and activate a virtual environment:**
    * **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    * Create a new folder in the root directory named `.streamlit`.
    * Inside `.streamlit`, create a file named `secrets.toml`.
    * Add your OpenWeatherMap API key to this file as shown below:
        ```toml
        OPENWEATHERMAP_API_KEY = "your_actual_api_key_here"
        ```

### Running the Application

Once the setup is complete, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in a new tab in your default web browser.

---

## 🛠️ Tech Stack

* **Framework:** [Streamlit](https://streamlit.io/)
* **Language:** Python
* **API:** [OpenWeatherMap API](https://openweathermap.org/api)
* **Libraries:**
    * `requests` for making API calls.
    * `Pillow` for image handling.

---

## 👨‍💻 Developed By

**Gopisetty Sai Charan**

* **Email:** [saicharangopisetty23@gmail.com](mailto:saicharangopisetty23@gmail.com)
* **Phone:** +91 9502996405
* **LinkedIn:** [linkedin.com/in/saicharangopisetty](https://www.linkedin.com/in/saicharangopisetty)
