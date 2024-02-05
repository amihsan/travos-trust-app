## 💡 About

This is the main repository of the TRAVOS app which includes both the frontend and backend logic of the application.

## View Demo (Deployed on AWS EC2)

http://ec2-13-50-151-220.eu-north-1.compute.amazonaws.com/

### 🧱 Built With

1. React
2. Python 3
3. Flask
4. npm
5. MongoDB

## ⚡ Getting Started

### ⚙️ Local Setup

1. Install MongoDB

2. Clone Git Repository, both frontend and backend.

3. Setup npm in frontend root:

   ```shell
   npm install
   ```

4. Setup virtual env in backend root:
   ```shell
   python -m venv venv
   ```
5. To activate the virtual environment:

   - On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   - On macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

   To install the Python dependencies specified in your `requirements.txt` file, use the following command:

   ```bash
   pip install -r requirements.txt
   ```

## 👟 Usage

### 🏠 Local Usage

1. Run local MongoDB

2. Run frontend:

   ```bash
   npm start
   ```

3. Run backend: after activate venv:

   For storing scenario details in MongoDB go to generate_scenario

   ```bash
   python insert_scenario_data.py
   ```

   and then in backend root:

   ```bash
   python app.py
   ```
