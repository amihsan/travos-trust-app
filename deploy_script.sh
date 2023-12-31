#!/bin/bash

# Run subsequent commands with elevated privileges
sudo su

# Change to the project directory
cd /home/ec2-user/travos-trust-app/

# Adjust ownership of the Git repository
sudo chown -R ec2-user:ec2-user /home/ec2-user/travos-trust-app

# Update the system
sudo yum update -y

# Pull the latest changes from the GitHub repository
sudo git pull https://github.com/amihsan/travos-trust-app.git

# Check the exit status of git pull
if [ $? -eq 0 ]; then
    echo "Git pull successful."
else
    echo "Git pull failed."
    # You might want to exit the script or handle the failure accordingly
    exit 1
fi

# Update the React app
cd frontend
npm install
npm run build

# Update the Flask API
cd ../backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Restart Frontend Service
sudo systemctl restart frontend

# Restart Backend Service
sudo systemctl restart backend

# Restart Nginx
sudo systemctl restart nginx

# Restart MongoDB Service
sudo systemctl restart mongod
