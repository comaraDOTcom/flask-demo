from flask import Flask
from flask_restful import Api

from fizzbuzz_controller import FizzBuzzController

app = Flask(__name__)
api = Api(app)

# forward any requests from this path to FizzBuzzController. this is called registering your routes
api.add_resource(FizzBuzzController, '/fizzbuzz/validate/<int:input_variable>')
#api.add_resource(FizzBuzzController, '/fizzbuzz/send/<int:input_variable>)

app.run(port=5000, debug=True)