# Import the python file containing the ML model
import model
# Import flask libraries
from flask import Flask, request, render_template, jsonify

# Initialize the flask class and specify the template directory
app = Flask(__name__, template_folder="templates")

# Default route set as 'home'
@app.route('/home')
def home():
	return render_template('home.html')

# Route 'classify' accepts GET request
@app.route('/classify', methods=['POST', 'GET'])
def classify_type():
	try:
		pregnancies = request.args.get('pregnancies')
		glucose = request.args.get('glucose')
		bloodpressure = request.args.get('bloodpressure')
		skinthickness = request.args.get('skinthickness')
		insulin = request.args.get('insulin')
		bmi = request.args.get('bmi')
		diabetespedigreefunction = request.args.get('diabetespedigreefunction')
		age = request.args.get('age')
		
		# Get the output from the classification model
		variety = model.classify(pregnancies, glucose, bloodpressure, bmi, diabetespedigreefunction, age, skinthickness, insulin)

		# Render the output in new HTML page
		return render_template('output.html', variety=variety)
	except:
		return 'Error'

# Run the Flask server
if(__name__ == '__main__'):
    app.run(debug=True)