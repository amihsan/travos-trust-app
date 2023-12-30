#!/bin/bash

sudo su

sudo yum update

# Update the React app
cd /home/ec2-user/travos-trust-app/frontend
npm install
npm run build

# Update the Flask API
cd /home/ec2-user/travos-trust-app/backend
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
