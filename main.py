
# Flask is the overall web framework
from flask import Flask, request

# joblib is used to unpickle the model
import joblib

# json is used to prepare the result
import json
import pandas as pd

# create new flask app here
app = Flask(__name__)

# helper function here

def churn_prediction(total_day_minutes, 
                    total_day_charge, 
                    total_eve_minutes, 
                    total_intl_charge,
                    total_intl_minutes,
                    total_night_charge,
                    total_night_minutes,
                    total_day_call,
                    features):
    
    # Load the model from the file
    model = joblib.load()
        
    # Construct the 2D matrix of values that .predict is expecting
    X = [["Total_Day_Minutes","Total_Day_Charge","Total_Eve_Minutes","Total_Eve_Charge",
        "Total_Intl_Charge","Total_Intl_Minutes","Total_Night_Charge","Total_Night_Minutes","Total_Day_Calls"]]
    
    data = pd.DataFrame(X)
    data.columns = features
    
    # Get a list of predictions and select only 1st
    predictions = model.predict(data)
    prediction = predictions[0]
    
    return {"predicted_class": prediction}

# defining routes here

@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data from the user in JSON format
    request_json = request.get_json()

    
    # Send it to our prediction function using ** to unpack the arguments
    result = churn_prediction(**request_json)

    # Return the result as a string with JSON format
    return json.dumps(result)


