#!/bin/bash

# Update the React app
sudo cd /home/ec2-user/travos-trust-app/frontend
sudo npm install
sudo npm run build

# Update the Flask API
sudo cd /home/ec2-user/travos-trust-app/backend
sudo python3 -m venv venv
sudo source venv/bin/activate
sudo pip install -r requirements.txt

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
