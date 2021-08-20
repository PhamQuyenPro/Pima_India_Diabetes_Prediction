# Import nessesary libraries
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load trained model
rf_model = joblib.load('rf.pkl')

# Load data to scaler
df = pd.read_csv('data.csv')
scaler = StandardScaler()
scaler.fit(df)

# Dictionary containing the mapping
variety_mappings = {0: 'Non Diabetes', 1: 'Diabetes'}

# Function for classification based on inputs
def classify(a, b, c, d, e, f, g, h):
	input_data = (float(a), float(b), float(c), float(d), float(e), float(f), float(g), float(h))
	input_data = list(input_data)

	# Add BMI Cat
	if input_data[3] > 0 and input_data[3] < 18.5:
		input_data.append(0)
	elif input_data[3] >= 18.5 and input_data[3] < 25:
		input_data.append(1)
	elif input_data[3] >= 25 and input_data[3] < 30:
		input_data.append(2)
	else:
		input_data.append(3)

	# Add Glucose Cat
	if input_data[1] > 0 and input_data[1] < 140:
		input_data.append(0)
	elif input_data[1] >= 140 and input_data[1] <= 199:
		input_data.append(1)
	else:
		input_data.append(2)

	# Add Insulin Cat
	if input_data[7] >= 16 and input_data[7] <= 166:
		input_data.append(0)
	else:
		input_data.append(1)

	# Pregnancies rate
	input_data.append(input_data[0] / input_data[5])

	# Glucose Insulin rate
	input_data.append(input_data[1] / input_data[7])

	# Scaling input data
	input_data_tp = tuple(input_data)
	input_data_np = np.array(input_data_tp)
	input_data_np_re = input_data_np.reshape(1, -1)
	std_input_data = scaler.transform(input_data_np_re)

	# Predict input data
	prediction = variety_mappings[rf_model.predict(std_input_data)[0]]

	return prediction

# print(classify(6, 148, 72, 33.6, 0.672, 50, 35, 255))


