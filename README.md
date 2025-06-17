# 🛡️ Phishing Email Detector

---

## Project Overview

The **Phishing Email Detector** is a lightweight and effective **Machine Learning-based web application** designed to classify incoming emails as either *phishing* or *legitimate*. This project leverages **Natural Language Processing (NLP)** techniques and the **FastAPI** framework to provide a real-time phishing detection service, contributing to enhanced cybersecurity measures for users.

---

## 🚀 Live Demo

Experience the Phishing Email Detector in action:

🌐 **Visit the deployed application:** [https://st-phishing-detector.onrender.com](https://st-phishing-detector.onrender.com)

Simply enter a sample email body into the text area and receive an instant prediction regarding its authenticity.

---

## ✨ Features

* **Real-time Classification:** Instantly classifies emails as phishing or legitimate.
* **Machine Learning Powered:** Utilizes a trained NLP model for accurate text classification.
* **User-Friendly Interface:** Provides a simple web interface for interaction.
* **Robust Backend:** Built with FastAPI for high performance and easy API development.
* **Automated Model Management:** Models are automatically downloaded and extracted upon deployment.
* **Cloud-Deployed:** Hosted on Render for continuous availability and scalability.

---

## 📈 Importance of This Project

This project addresses critical real-world cybersecurity challenges by offering a practical solution for identifying malicious emails. Its significance stems from:

* **Cybersecurity Enhancement:** Directly helps users avoid common phishing scams, safeguarding personal and sensitive information.
* **Proactive Threat Detection:** Identifies potentially harmful email content before users can click on malicious links or divulge confidential data.
* **Applied ML & NLP:** Demonstrates the practical application of advanced machine learning and natural language processing techniques for text classification.
* **Cloud-Native Deployment:** Showcases seamless cloud deployment using Render, ensuring accessibility and ease of use.
* **Educational Value:** Serves as an excellent resource for students, developers, and cybersecurity enthusiasts interested in machine learning, NLP, FastAPI, and full-stack application deployment.

---

## 💻 Technologies Used

* **Python:** The core programming language for the application.
* **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
* **Scikit-learn:** Used for machine learning model training and inference.
* **NLTK (Natural Language Toolkit):** Utilized for text preprocessing in NLP.
* **Render:** Cloud platform for deploying and hosting the web service.
* **Git & GitHub:** For version control and collaborative development.

---

## 🧪 Local Setup Instructions

To set up and run the Phishing Email Detector on your local machine, follow these steps:

### 1. Clone the Repository

Begin by cloning the project repository to your local system:

```bash
git clone [https://github.com/sanjanatanna/phishing-detector.git](https://github.com/sanjanatanna/phishing-detector.git)
cd phishing-detector
````

### 2\. Install Dependencies

Navigate into the cloned directory and install the necessary Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3\. Run the FastAPI App

Start the FastAPI development server. The `--reload` flag enables auto-reloading upon code changes.

```bash
uvicorn app.inference_api:app --reload
```

### 4\. Access the API

Once the server is running, you can access the application's API endpoints:

  * **Interactive API Documentation (Swagger UI):**

    ```bash
    http://localhost:8000/docs
    ```

    This interface allows you to test the API endpoints directly from your browser.

  * **Prediction Endpoint:**

    ```bash
    http://localhost:8000/predict
    ```

    This is the primary endpoint for submitting email content for classification.

-----

## ☁️ Deployment Notes (Render)

This project is configured for seamless deployment on Render.

### 🔄 Model Auto-Download

One of the key features for deployment is that the necessary model files are **automatically downloaded and extracted at runtime** when the application is deployed to Render. This eliminates the need for manual model uploads, streamlining the deployment process—simply push your code, and Render handles the rest.

### 🚀 Render Start Command

Render executes the application using the following command, ensuring it binds to the correct host and port:

```bash
uvicorn app.inference_api:app --host 0.0.0.0 --port $PORT
```

### ⚙️ `.render.yaml` Configuration

The repository includes a `.render.yaml` file, which specifies the deployment configuration for Render. This file defines the service type, build commands, and runtime environment variables.

```yaml
services:
  - type: web
    name: phishing-detector
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.inference_api:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PORT
        value: "10000"
    plan: free
```

-----

## 📂 Project Structure

The project is organized into a clear and modular structure to enhance maintainability and understanding:

```
phishing-detector/
├── app/
│   └── inference_api.py      # Main FastAPI application logic and prediction endpoint
├── models/                   # Directory where pre-trained ML models are stored/downloaded
├── frontend/                 # Contains static assets for the web user interface (HTML/CSS/JS)
├── requirements.txt          # Lists all Python dependencies required by the project
├── .render.yaml              # Render deployment configuration file
└── README.md                 # Project documentation (this file)
```

-----

## 📝 License

This project is open-sourced under the [MIT License](https://www.google.com/search?q=LICENSE). Feel free to use, modify, and distribute it for personal or commercial purposes.

```
```
