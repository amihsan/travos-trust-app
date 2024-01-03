from flask import Blueprint, jsonify, request
from evaluation.evaluation_logic import perform_evaluation
from pymongo import MongoClient
import os
from dotenv import load_dotenv

bp = Blueprint('main', __name__)

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB connection details from environment variables
mongodb_uri = os.getenv('MONGODB_URI')
database_name = os.getenv('DATABASE_NAME')

# Connect to MongoDB
client = MongoClient(mongodb_uri)
db = client[database_name]

# Default Route: Hello From Ihsan
@bp.route('/')
def hello_from_ihsan():
    
    try:
      return 'Hello From Backend'
    
    except Exception as e:
        return handle_error('get_scenario_details', f'An error occurred: {str(e)}')
    
# Route 1: Get All Scenarios List
@bp.route('/api/getAllScenarios')
def get_all_scenarios():
    try:
        collections = db.list_collection_names()
        return collections
    
    except Exception as e:
        return handle_error('get_all_scenarios', f'An error occurred: {str(e)}')
    
# Route 2: Get Scenario Details
@bp.route('/api/getScenarioDetails/<int:scenario_number>')
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

# Route 3: Start Evaluation
@bp.route('/api/startEvaluation', methods=['POST'])
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