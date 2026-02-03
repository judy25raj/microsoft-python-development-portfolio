<h1 align="center">Flask Web Application – Azure Deployment</h1>

<p align="center">
  Python • Flask • Cloud Deployment • Configuration • Web Services
</p>

<hr/>

## 🧠 Overview
This project is a Flask-based web application structured for cloud deployment on **Microsoft Azure**.
It demonstrates how to build a lightweight web service, configure environments, and package an app for cloud hosting.

The focus is on clean application structure, configuration, and deployment readiness.

## 🎯 Capabilities Demonstrated
- Flask routing and template rendering
- Static asset management (CSS/JS)
- Environment-based configuration
- Deployment-ready project structure
- Cloud fundamentals for web services

## 📂 Project Structure
```
microsoft-python-flask-azure-deployment/
├── app.py              # Flask entry point
├── templates/          # HTML templates
├── static/css/         # Stylesheets
├── docs/               # Deployment notes
├── requirements.txt
└── README.md
```

## ▶ How to Run Locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

## ☁️ Cloud Deployment (Azure)
This project is structured to be deployed to Azure App Service or a container-based service.
Configuration can be externalized using environment variables for secrets and runtime settings.

## 🧠 Engineering Value
- Demonstrates web-service deployment patterns
- Shows cloud-ready application design
- Supports scalable hosting scenarios
