# Microsoft Python – Intelligent Blog App (Flask)

A minimal Flask web app project (with templates + static assets) and basic pytest tests.

## What’s inside
- `app.py` – Flask application entry point
- `templates/` – HTML templates
- `static/` – JS/CSS assets
- `tests/` – pytest tests

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open: http://127.0.0.1:5000

## Run tests
```bash
pytest -q
```

## Notes
This folder is cleaned for GitHub (removed cache folders like `__pycache__` and `.pytest_cache`).
