
# i-love-cats

A small Django-based API that serves a dynamic profile endpoint. Each request to /me returns profile information plus a freshly-fetched cat fact from an external API.

This repository is implemented in Python (100%) and is designed to be lightweight, easy to understand, and simple to deploy (tested on Railway).

Key highlights
- Django REST endpoint: GET /me → returns profile + a dynamic cat fact
- External API integration using the requests library
- Clean, structured JSON response suitable for frontends or integrations


Demo
- Repo: https://github.com/Best-wale/i-love-cats
- Live (Railway): [<paste Railway app URL >](https://i-love-cats-production.up.railway.app/me/)

Features
- /me endpoint returns:
  - personal profile metadata (name, role, location, skills, socials)
  - a randomly fetched cat fact from an external API (configured via env var)
- Simple codebase that's easy to read and extend
- Configurable through environment variables for secure credentials and API URLs

Getting started (local)
Prerequisites
- Python 3.10+ (or recommended version)
- pip
- virtualenv (recommended)

Quick start
1. Clone the repo
   git clone https://github.com/Best-wale/i-love-cats.git
   cd i-love-cats

2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows (PowerShell)

3. Install dependencies
   pip install -r requirements.txt


5. Run migrations (if the project uses them)
   python manage.py migrate

6. Run the dev server
   python manage.py runserver

7. Open the endpoint
   http://127.0.0.1:8000/me

Example request
curl http://127.0.0.1:8000/me

Example response
{
  "status": "success",
  "user": {
    "email": "Bestigbekele5@gmail.com",
    "name": "Best Igbekele",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-19T10:59:38.048185+00:00",
  "fact": "Cats, especially older cats, do get cancer. Many times this disease can be treated successfully."
}

Configuration / Environment variables
- DJANGO_ALLOWED_HOSTS — Comma-separated allowed hosts )
- CAT_API_URL — URL for cat fact API (default: https://catfact.ninja/fact)

Railway deployment notes
- Push your repo to GitHub.
- Create a new Railway project and connect to the GitHub repo.
- Configure the start command (e.g., gunicorn config.wsgi:application or python manage.py runserver 0.0.0.0:$PORT depending on your Railway setup).
- Enable migrations/run management commands in Railway if needed.




Notes
- The repository is pure Python (100% as detected). Adjust the instructions above to match any project-specific files (requirements.txt, or exact settings names).

````
