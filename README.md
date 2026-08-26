# Kabindra Karki — Django Portfolio

A professional full-stack developer portfolio built with **Python, Django, HTML5, CSS3, and JavaScript**.

## Features

- Responsive premium one-page portfolio
- Dark/light theme switcher
- Animated section reveals and skill bars
- Django-powered projects, skills, and education
- Project case-study pages
- Contact form saved to the Django database
- Gmail notification for every valid contact-form submission
- Visitor email configured as Reply-To for easy replies
- Django Admin for reviewing messages and updating portfolio content
- Downloadable Word CV
- Mobile navigation and responsive layouts
- SEO-friendly title and meta description

## Run locally

```bash
python -m venv .venv
```

### Windows PowerShell

If PowerShell blocks virtual-environment activation, run this first in the current PowerShell window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_portfolio
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

Django Admin: `http://127.0.0.1:8000/admin/`

## Enable Gmail notifications

The contact form always saves valid messages to the database. To also receive each message at **karkikabindra98@gmail.com**, configure Gmail SMTP credentials locally or in your hosting provider.

1. Turn on **2-Step Verification** for the Google account used to send mail.
2. Create a **Google App Password** for the portfolio. Use the generated app password, not your normal Gmail password.
3. Copy `.env.example` to a new file named `.env` in the project root.
4. Replace `your-16-character-gmail-app-password` with your Google App Password.
5. Keep `.env` private. It is already ignored by Git through `.gitignore`.
6. Restart the Django development server after changing `.env`.

Example `.env` values:

```env
EMAIL_HOST_USER=karkikabindra98@gmail.com
EMAIL_HOST_PASSWORD=YOUR_GOOGLE_APP_PASSWORD
DEFAULT_FROM_EMAIL=karkikabindra98@gmail.com
PORTFOLIO_OWNER_EMAIL=karkikabindra98@gmail.com
```

When a visitor submits the contact form:

1. The message is stored in Django Admin.
2. Django sends a notification to `PORTFOLIO_OWNER_EMAIL`.
3. Clicking **Reply** in Gmail replies directly to the visitor because their address is set as `Reply-To`.
4. If Gmail is temporarily unavailable, the database copy remains saved.

## Test the contact form

Run the site and submit a test message from the Contact section. Then check:

- Your Gmail inbox and Spam folder.
- Django Admin under Contact Messages.

If the database message appears but Gmail does not, verify the App Password and environment variables, then restart the server.

## Before publishing

1. Set a strong `DJANGO_SECRET_KEY` environment variable.
2. Set `DJANGO_DEBUG=False` in production.
3. Add your real deployment domain to `DJANGO_ALLOWED_HOSTS`.
4. Add the same email variables from `.env` to the deployment platform's environment/secrets settings. Never upload `.env` to GitHub.
5. Add GitHub and live project URLs in Django Admin as they become available.
6. Replace the Word CV in `static/resume/` whenever you update your resume.
7. For production, PostgreSQL is recommended instead of SQLite.

## Main editable content

Your initial portfolio data is in:

`core/management/commands/seed_portfolio.py`

After seeding, you can update everything in Django Admin without editing code.
