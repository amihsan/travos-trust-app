#!/bin/bash
sudo su
sudo yum update

# Project Root
cd travos-trust-app/

# Log
git pull https://github.com/amihsan/travos-trust-app.git
echo "Updating changes from Github Repo"

# Log
echo "Updating the React app..."
cd /home/ec2-user/travos-trust-app/frontend
npm install
npm run build


# Restart Frontend Service
sudo systemctl restart frontend
echo "Frontend service restarted successfully."

# Restart Nginx
sudo systemctl restart nginx
echo "Nginx restarted successfully."

# Restart MongoDB Service
sudo systemctl restart mongod
echo "MongoDB service restarted successfully."

# Restart Gunicorn (Flask)
sudo systemctl restart gunicorn
echo "Gunicorn restarted successfully."
