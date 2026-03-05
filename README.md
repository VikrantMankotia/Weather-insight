# 🌦 Weather Insight App

A simple web application built using **Python and Streamlit** that provides real-time weather information for any city using the OpenWeather API.

This project demonstrates how to integrate external APIs, manage environment variables securely, and deploy a Python web application to the cloud.

---

# 🚀 Live Demo

The application is deployed using **Streamlit Community Cloud**.

🔗 Live Application
https://weather-app-vikrant.streamlit.app/

---

# 📌 Features

* Search weather information by entering a city name
* Displays real-time weather data
* Shows key weather metrics including:

  * 🌡 Temperature
  * 💧 Humidity
  * 🌬 Wind Speed
  * ☁ Weather Condition
* Clean and simple user interface
* Handles invalid city inputs with error messages
* Secure API key handling using environment variables

---

# 🛠 Tech Stack

## Python

Python is the main programming language used to build the application logic, handle API requests, and process data.

## Streamlit

Streamlit is a Python framework used to quickly build and deploy interactive web applications without requiring frontend technologies like HTML, CSS, or JavaScript.

It allows developers to create UI components using simple Python commands such as:

* `st.title()`
* `st.text_input()`
* `st.button()`
* `st.metric()`

Streamlit automatically converts Python code into a web interface.

## Requests Library

The **Requests** library is used to send HTTP requests to external APIs and retrieve data.

Example:

```python
requests.get(API_URL)
```

This allows the application to fetch weather data from the OpenWeather API.

## OpenWeather API

The application uses the **OpenWeather API** to retrieve real-time weather data for any city worldwide.

The API returns weather information in **JSON format**, which is then processed and displayed in the app.

Example API request:

https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}

---

# 🔐 Environment Variables

To protect sensitive information such as API keys, the application uses environment variables.

## Local Development

Create a `.env` file:

```text
WEATHER_API_KEY=your_api_key_here
```

The `.env` file is included in `.gitignore` so that it is not uploaded to GitHub.

---

## Deployment

When the application is deployed to **Streamlit Cloud**, the API key is stored using **Streamlit Secrets Manager**.

Example configuration:

```toml
WEATHER_API_KEY="your_api_key_here"
```

This ensures the API key remains secure in production.

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/weather-insight.git
```

Navigate into the project directory:

```bash
cd weather-insight
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

Run the application locally:

```bash
streamlit run weather_app.py
```

---

# ☁ Deployment

The project is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push the project to GitHub
2. Connect the repository to Streamlit Cloud
3. Configure API key using Secrets Manager
4. Deploy the application

---

# 📚 What I Learned

Through this project, I gained practical experience with:

* API integration using Python
* Sending HTTP requests and handling JSON responses
* Managing environment variables securely
* Using `.env` and `.gitignore`
* Deploying Python applications to the cloud
* Debugging production environment issues
* Building simple web applications using Streamlit

---

# 🎯 Purpose of the Project

This project was built to understand the practical workflow of:

* Building a small web application
* Integrating third-party APIs
* Managing secrets securely
* Deploying applications to a cloud platform

---

# 👨‍💻 Author

**Vikrant Mankotia**

GitHub
https://github.com/VikrantMankotia
