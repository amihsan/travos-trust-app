#!/bin/bash

sudo su

sudo yum update

ls

cd travos-trust-app/

ls

# Update the React app
cd frontend/
ls
npm install
npm run build

cd ..

# Update the Flask API
cd backend/
python3 -m venv venv       
source venv/bin/activate     
pip install -r requirements.txt

# Restart Gunicorn (Flask)
sudo systemctl restart gunicorn

# Restart Frontend Service
sudo systemctl restart frontend

# Restart Backend Service
sudo systemctl restart backend

# Restart Nginx
sudo systemctl restart nginx

# Restart MongoDB Service
sudo systemctl restart mongod
