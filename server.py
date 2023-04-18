from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)
# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.
    
@app.route('/process1', methods = ['POST'] )
def processOne():
	data = request.json #this is the data sent from client to server 
	result = process1(data)
	return jsonify(result) #send result back to client

@app.route('/process2', methods = ['POST'] )
def processTwo():
	data = request.json #this is the data sent from client to server 
	result = process2(data)
	return jsonify(result) #send result back to client


if __name__ == "__main__":
    app.run(host = '192.168.1.14', debug=True)
