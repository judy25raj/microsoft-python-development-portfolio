<h1 align="center">Intelligent Blog Application (Flask)</h1>

<p align="center">
  Python • Flask • Web Application • Templates • Testing
</p>

<hr/>

## 🧠 Overview
This project is a lightweight Flask-based web application that demonstrates backend routing, template rendering, static asset handling, and basic automated testing.

It represents a clean, production-style micro web service suitable for content-driven applications and internal tools.

## 🎯 Capabilities Demonstrated
- Flask application structure and routing
- HTML template rendering (Jinja2)
- Static asset management (CSS/JS)
- Configuration via virtual environments
- Automated testing with pytest

## 📂 Project Structure
```
microsoft-python-intelligent-blog-app/
├── app.py              # Flask application entry point
├── templates/          # HTML templates
├── static/             # CSS/JS assets
├── tests/              # pytest test cases
├── requirements.txt
└── README.md
```

## ▶ How to Run
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

## ▶ Run Tests
```bash
pytest -q
```

## 🧠 Engineering Value
- Demonstrates MVC-style web application design
- Shows clean separation of concerns
- Supports test-driven development
- Suitable for small content or internal apps
