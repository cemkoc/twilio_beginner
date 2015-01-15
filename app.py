from flask import Flask
from flask import request
from twilio import twiml
import os

app = Flask(__name__)

@app.route('/caller', methods=['POST'])
def caller():
	response = twiml.Response()
	response.enqueue("Call Queue")
	return str(response)


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)
	
