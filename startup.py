#!/usr/bin/env python
import os
import sys
import subprocess
import time

def run_command(command, description):
    """Run a command and return the result"""
    print(f"Running {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                              text=True)
        print(f"{description} completed successfully.")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{description} failed with exit code {e.returncode}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def main():
    print("Starting NerdHub deployment process...")
    
    # Change to the app directory
    app_dir = '/app'
    if os.path.exists(app_dir):
        os.chdir(app_dir)
        print(f"Changed to directory: {os.getcwd()}")
    
    # Run migrations
    if not run_command("python manage.py migrate --noinput", "database migrations"):
        print("Exiting due to migration failure.")
        sys.exit(1)
    
    # Collect static files
    if not run_command("python manage.py collectstatic --noinput --verbosity=0", "static file collection"):
        print("Warning: Static file collection failed, but continuing...")
    
    # Start the server
    print("Starting Gunicorn server...")
    os.execvp("gunicorn", ["gunicorn", "nerdhub.wsgi", "--log-file", "-"])

if __name__ == "__main__":
    main()