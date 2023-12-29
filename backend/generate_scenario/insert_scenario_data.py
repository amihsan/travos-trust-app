from pymongo import MongoClient

# Connect to MongoDB  for local use
client = MongoClient("mongodb://localhost:27017/") 

db = client['development_database'] 


#For  Production
# client = MongoClient("mongodb://<userid:psw@public_ip>:27017/?authMechanism=DEFAULT/") 
# db = client['production_database']  # for deployment

# With Mongodb atlas
# client = MongoClient('mongodb+srv://<userid:psw>@cluster0.egvwq.mongodb.net/')


# Example data for Scenario 1
scenario1_data = {
  "users": ["A", "B", "C", "D"],
  "observations": [
    {"sender": "A", "recipient": "B", "message": "Redecentralization of the Web"},
    {"sender": "D", "recipient": "C", "message": "Web of Things"},
    {"sender": "C", "recipient": "B", "message": "Web Assembly"},
    {"sender": "B", "recipient": "D", "message": "Semantic Web and Linked Open Data"},
    {"sender": "C", "recipient": "A", "message": "Redecentralization of the Web"},
    {"sender": "D", "recipient": "A", "message": "Web-based learning"}
  ],
  "history": {
    "A": {
      "B": {"url": "https://example.com/Semantic-Web", "data": [9, 14]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [18, 11]},
      "D": {"url": "https://example.com/Semantic-Web", "data": [2, 15]}
    },
    "B": {
      "A": {"url": "https://example.com/Semantic-Web", "data": [17, 5]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [3, 0]},
      "D": {"url": "https://example.com/Web-Assembly", "data": [18, 5]}
    },
    "C": {
      "A": {"url": "https://example.com/Linked-Data", "data": [4, 1]},
      "B": {"url": "https://example.com/Web-based-learning", "data": [3, 1]},
      "D": {"url": "https://example.com/Web-of-Things", "data": [7, 3]}
    },
    "D": {
      "A": {"url": "https://example.com/Web-Assembly", "data": [3, 0]},
      "B": {"url": "https://example.com/Linked-Data", "data": [6, 2]},
      "C": {"url": "https://example.com/Web-Assembly", "data": [15, 46]}
    }
  }
}


# Example data for Scenario 2
scenario2_data = {
  "users": ["A", "B", "C", "D"],
  "observations": [
    {"sender": "A", "recipient": "B", "message": "Redecentralization of the Web"},
    {"sender": "A", "recipient": "D", "message": "Web of Things"},
    {"sender": "C", "recipient": "B", "message": "Web Assembly"},
    {"sender": "C", "recipient": "D", "message": "Semantic Web and Linked Open Data"},
    {"sender": "D", "recipient": "B", "message": "Redecentralization of the Web"},
    {"sender": "D", "recipient": "A", "message": "Web-based learning"}
  ],
  "history": {
    "A": {
      "B": {"url": "https://example.com/Semantic-Web", "data": [9, 20]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [18, 11]},
      "D": {"url": "https://example.com/Semantic-Web", "data": [2, 15]}
    },
    "B": {
      "A": {"url": "https://example.com/Semantic-Web", "data": [17, 5]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [3, 0]},
      "D": {"url": "https://example.com/Web-Assembly", "data": [18, 5]}
    },
    "C": {
      "A": {"url": "https://example.com/Linked-Data", "data": [4, 1]},
      "B": {"url": "https://example.com/Web-based-learning", "data": [3, 1]},
      "D": {"url": "https://example.com/Web-of-Things", "data": [7, 3]}
    },
    "D": {
      "A": {"url": "https://example.com/Web-Assembly", "data": [3, 0]},
      "B": {"url": "https://example.com/Linked-Data", "data": [6, 2]},
      "C": {"url": "https://example.com/Web-Assembly", "data": [15, 46]}
    }
  }
}


# Example data for Scenario 3
scenario3_data = {
  "users": ["A", "B", "C", "D"],
  "observations": [
    {"sender": "B", "recipient": "A", "message": "Redecentralization of the Web"},
    {"sender": "C", "recipient": "D", "message": "Web of Things"},
    {"sender": "D", "recipient": "A", "message": "Web Assembly"},
    {"sender": "A", "recipient": "B", "message": "Semantic Web and Linked Open Data"},
    {"sender": "B", "recipient": "C", "message": "Redecentralization of the Web"},
    {"sender": "C", "recipient": "D", "message": "Web-based learning"}
  ],
  "history": {
    "A": {
      "B": {"url": "https://example.com/Semantic-Web", "data": [9, 30]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [18, 11]},
      "D": {"url": "https://example.com/Semantic-Web", "data": [2, 15]}
    },
    "B": {
      "A": {"url": "https://example.com/Semantic-Web", "data": [17, 5]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [3, 0]},
      "D": {"url": "https://example.com/Web-Assembly", "data": [18, 5]}
    },
    "C": {
      "A": {"url": "https://example.com/Linked-Data", "data": [4, 1]},
      "B": {"url": "https://example.com/Web-based-learning", "data": [3, 1]},
      "D": {"url": "https://example.com/Web-of-Things", "data": [7, 3]}
    },
    "D": {
      "A": {"url": "https://example.com/Web-Assembly", "data": [3, 0]},
      "B": {"url": "https://example.com/Linked-Data", "data": [6, 2]},
      "C": {"url": "https://example.com/Web-Assembly", "data": [15, 46]}
    }
  }
}


# Example data for Scenario 4
scenario4_data = {
  "users": ["A", "B", "C", "D"],
  "observations": [
    {"sender": "D", "recipient": "A", "message": "Redecentralization of the Web"},
    {"sender": "A", "recipient": "B", "message": "Web of Things"},
    {"sender": "B", "recipient": "C", "message": "Web Assembly"},
    {"sender": "C", "recipient": "D", "message": "Semantic Web and Linked Open Data"},
    {"sender": "D", "recipient": "C", "message": "Redecentralization of the Web"},
    {"sender": "A", "recipient": "C", "message": "Web-based learning"}
  ],
  "history": {
    "A": {
      "B": {"url": "https://example.com/Semantic-Web", "data": [9, 40]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [18, 11]},
      "D": {"url": "https://example.com/Semantic-Web", "data": [2, 15]}
    },
    "B": {
      "A": {"url": "https://example.com/Semantic-Web", "data": [17, 5]},
      "C": {"url": "https://example.com/Web-based-learning", "data": [3, 0]},
      "D": {"url": "https://example.com/Web-Assembly", "data": [18, 5]}
    },
    "C": {
      "A": {"url": "https://example.com/Linked-Data", "data": [4, 1]},
      "B": {"url": "https://example.com/Web-based-learning", "data": [3, 1]},
      "D": {"url": "https://example.com/Web-of-Things", "data": [7, 3]}
    },
    "D": {
      "A": {"url": "https://example.com/Web-Assembly", "data": [3, 0]},
      "B": {"url": "https://example.com/Linked-Data", "data": [6, 2]},
      "C": {"url": "https://example.com/Web-Assembly", "data": [15, 46]}
    }
  }
}


# Insert data into Scenario 1 collection
scenario1_collection = db['scenario_1']
scenario1_collection.insert_one(scenario1_data)

# Insert data into Scenario 2 collection
scenario2_collection = db['scenario_2']
scenario2_collection.insert_one(scenario2_data)

# Insert data into Scenario 3 collection
scenario3_collection = db['scenario_3']
scenario3_collection.insert_one(scenario3_data)

# Insert data into Scenario 4 collection
scenario4_collection = db['scenario_4']
scenario4_collection.insert_one(scenario4_data)

# Close the MongoDB connection
client.close()
