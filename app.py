from flask import Flask, jsonify, request

app = Flask(__name__)

#Below is simple mock data for demonstration
mack_data = {"data": ["python", "Java", "Php", ".net", "golang", "C++"]}

processed_data = {}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
	return jsonify(mock_data)


@app.route('/process-data', methods=['POST'])
def process_data():
	global processed_data
	data = mock_data["data"]
	# task related to process data by converting text to upper case
	processed_data = [item.upper() for item in data]
	return jsonify({"processed": processed_data})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
	return jsonify({"processed_data": processed_data})

if __name =='__main__':
	app.run(debug=True)

	
