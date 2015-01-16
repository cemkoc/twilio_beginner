from flask import Flask
from flask import request
from twilio import twiml
import os

app = Flask(__name__)

@app.route('/caller', methods=['POST'])
def caller():
	response = twiml.Response()
	response.enqueue("Christmas Call Queue", waitUrl="/wait")
	return str(response)

@app.route('/wait', methods=['POST'])
def wait():
	response = twiml.Response()
	response.say("Thank you for calling little grinch.")
	response.say("You are number %s in the queue." % request.form['QueuePosition'])
	return str(response)

@app.route('/agent', methods['POST'])
def agent():
	response = twiml.Response()
	with response.dial() as dial:
		dial.queue("Christmas Call Queue")
	return str(response)
	


if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.debug = True
	app.run(host='0.0.0.0', port=port)