#!/bin/bash
cd /home/ec2-user/

# Update the system
sudo yum update

# Change to the project directory
cd /home/ec2-user/travos/travos-trust-app/

# Pull the latest changes from the GitHub repository
git stash
git fetch origin main
git merge origin/main

# Check the exit status of git pull
if [ $? -eq 0 ]; then
    echo "Git merge successful."
else
    echo "Git merge failed."
    # You might want to exit the script or handle the failure accordingly
    exit 1
fi

# Update the React app
cd frontend
npm update -g
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
