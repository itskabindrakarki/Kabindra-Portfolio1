# Deploy Kabindra Karki Portfolio on Render

## 1. Push the project to GitHub
Create a new GitHub repository, then from this project folder run:

```powershell
git init
git add .
git commit -m "Prepare portfolio for deployment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

## 2. Deploy on Render
1. Sign in to Render using GitHub.
2. Open **Blueprints** and create a new Blueprint.
3. Select this repository. Render will read `render.yaml`.
4. Before completing the deployment, provide the secret environment variables requested by the Blueprint.

Important environment values:

- `EMAIL_HOST_USER` = your Gmail address
- `EMAIL_HOST_PASSWORD` = your Google App Password, not your normal Gmail password
- `DEFAULT_FROM_EMAIL` = your Gmail address
- `DJANGO_ALLOWED_HOSTS` = initially your Render hostname; after adding your domain, use a comma-separated value such as `yourdomain.com,www.yourdomain.com`
- `DJANGO_CSRF_TRUSTED_ORIGINS` = `https://yourdomain.com,https://www.yourdomain.com`

Render automatically provides its own external hostname to Django through `RENDER_EXTERNAL_HOSTNAME`, so the initial `.onrender.com` URL works before you attach your domain.

## 3. Test the Render URL
Once deployed, open the generated `https://...onrender.com` URL and test:
- Home page
- Project detail pages
- Contact form
- `/admin/`

Create the admin account from the Render Shell:

```bash
python manage.py createsuperuser
```

## 4. Attach your custom domain
In Render:
1. Open the web service.
2. **Settings > Custom Domains > Add Custom Domain**.
3. Add the root domain or `www` domain.
4. Render will show the DNS record(s) to add at your domain registrar/DNS provider.
5. Add those DNS records at your domain provider.
6. Return to Render and verify the domain.

Then update:

`DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`

`DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com`

Render provisions HTTPS/TLS automatically for verified custom domains.

## 5. Contact email
The contact form saves every message to PostgreSQL and sends a notification to `karkikabindra98@gmail.com` when Gmail SMTP variables are configured correctly.
