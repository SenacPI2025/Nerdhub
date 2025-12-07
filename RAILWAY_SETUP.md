# Railway Deployment Setup Guide

This guide will help you set up your NerdHub application on Railway with PostgreSQL.

## Prerequisites

1. A Railway account (railway.app)
2. Your GitHub repository connected to Railway
3. This repository cloned locally

## Step 1: Create PostgreSQL Database on Railway

1. Go to your Railway dashboard
2. Click "New Project"
3. Select "Provision PostgreSQL"
4. Wait for the database to be provisioned

## Step 2: Configure Environment Variables

In your Railway project, add these environment variables:

```
DATABASE_URL=postgresql://username:password@host:port/database_name
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_ALLOWED_HOSTS=your-domain.railway.app,localhost
DEBUG=false
```

Note: Railway automatically provides the DATABASE_URL when you provision a PostgreSQL database.

## Step 3: Deploy the Application

Push your changes to GitHub:

```bash
git add .
git commit -m "Add database schema documentation and Railway setup guide"
git push origin main
```

Railway will automatically detect the changes and start the deployment.

## Step 4: Run Initial Setup Commands

After deployment, you need to run these commands in the Railway console:

1. Run migrations:
   ```bash
   python manage.py migrate
   ```

2. Collect static files:
   ```bash
   python manage.py collectstatic --noinput
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin user.

## Step 5: Verify Deployment

1. Visit your application URL provided by Railway
2. Test the admin panel at `/painel/`
3. Ensure all functionality works correctly

## Troubleshooting

### Common Issues

1. **Database Connection Error**: Check that DATABASE_URL is correctly set in environment variables
2. **Static Files Not Loading**: Ensure Whitenoise is configured and collectstatic was run
3. **Missing Dependencies**: Verify all packages in requirements.txt are installed

### Checking Logs

You can view application logs in the Railway dashboard:
1. Go to your project
2. Click on your application
3. Select "Logs" tab

### Running Commands on Railway

To run Django commands on Railway:
1. Go to your project in Railway
2. Click on your application
3. Select "Console" tab
4. Run your commands there

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection string | postgresql://user:pass@host:port/db |
| DJANGO_SECRET_KEY | Django secret key | your-secret-key-here |
| DJANGO_ALLOWED_HOSTS | Allowed domains | your-domain.railway.app,localhost |
| DEBUG | Debug mode (should be false in production) | false |

## Database Schema

Refer to `DATABASE_SCHEMA.md` for detailed database structure information.

## Support

If you encounter issues:
1. Check the Railway documentation
2. Review application logs
3. Verify environment variables are correctly set