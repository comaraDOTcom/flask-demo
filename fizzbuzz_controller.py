# controllers are routers. we put our routes for incoming requests.
# these are the mapping class for external request to internal request.
# we handle these requests with controllers.

# must define the http get method, post method etc.

from flask_restful import Resource

from fizzbuzz_service import FizzBuzzService

# Adding comment from Atom git service


class FizzBuzzController(Resource):
    def get(self, input_variable):
        return FizzBuzzService.validate(input_variable)
