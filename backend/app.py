from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_cors import CORS
from evaluation.evaluation_logic import perform_evaluation
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Retrieve MongoDB connection details from environment variables
mongodb_uri = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/')
database_name = os.environ.get('DATABASE_NAME', 'development_database')

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client[database_name]

# Default Route: Hello From Ihsan
@app.route('/')
def hello_from_ihsan():
    return 'Hello From Ihsan'

# Route 1: Get Scenario Details
@app.route('/api/getScenarioDetails/<int:scenario_number>')
def get_scenario_details(scenario_number):
    try:
        scenario_collection = db[f'scenario_{scenario_number}']
        scenario_details = scenario_collection.find_one()

        if scenario_details is None:
            return jsonify({'error': f'Scenario {scenario_number} not found'}), 404

        # Convert ObjectId to string for JSON serialization
        scenario_details['_id'] = str(scenario_details['_id'])

        return jsonify(scenario_details)
    
    except Exception as e:
        return handle_error('get_scenario_details', f'An error occurred: {str(e)}')

# Route 2: Start Evaluation
@app.route('/api/startEvaluation', methods=['POST'])
def start_evaluation():
    try:
        selected_scenario = request.json.get('scenario')

        scenario_collection = db[f'scenario_{selected_scenario}']
        scenario_details = scenario_collection.find_one()

        if scenario_details is None:
            return jsonify({'error': f'Selected scenario {selected_scenario} not found'}), 404

        evaluation_results = perform_evaluation(scenario_details)

        return jsonify({'message': f'Evaluation started for scenario {selected_scenario}', 'results': evaluation_results})
    
    except Exception as e:
        return handle_error('start_evaluation', f'An error occurred: {str(e)}')

def handle_error(route_name, error_message, status_code=500):
    # Simplified error handling function
    return jsonify({'error': error_message}), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
