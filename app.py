from flask import Flask
from flask import request
from twilio import twiml
from twilio.rest import TwilioRestClient
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
	response.say("Thank you for calling the grinch hotline.")
	response.say("You are number %s in the queue." % request.form['QueuePosition'])
	client = TwilioRestClient(ACda7d5ef08c17d20a529a663cde08e21b, 
		ACda7d5ef08c17d20a529a663cde08e21b)
	client.sms.message.create(to="+17770000", from="+14152983952", 
		body="Hey someone is in the queue. Call to help !")
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