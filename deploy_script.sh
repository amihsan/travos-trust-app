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
systemctl restart gunicorn

# Restart Frontend Service
systemctl restart frontend

# Restart Backend Service
systemctl restart backend

# Restart Nginx
systemctl restart nginx

# Restart MongoDB Service
systemctl restart mongod
