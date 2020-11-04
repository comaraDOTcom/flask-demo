## Flask API Demo
Based off "RestAPI development with Python and Flask" given by [Rasim Sen](https://github.com/rasimsen/restful-api-with-database-with-python-flask)
on 19/10/2020.

For an application, there are two possible architectures:

**Monolithic architecture:** (3 layer pattern - presentation/ui (front end), business
layer(implementing business logic), data access layer (database)).
We are creating one monolith in one big bucket. It is not a good practice to directly
connect the fronted to backend. i.e. big bucket that contains all the components.
**_For example_** on the on the backend we require more optimisation for performance
(not needed for the front end).


**Microservice architecture:** splits the backend into many smaller components. On the
backend side we prefer not to have all components in the same folder ( **_i.e._**
user_profile, shopping cart etc) because each component has different dynamics. But it
appears like they are together on the frontend..However on the back end, how it may work like so:
  * **_Search component_** might use elasticsearch as framework
  * **_Shopping cart_** might use NoSQL database

Each microservice can have a different framework and different technology. Another
advantage is scalablility. If we were to put the app in a  kubernetes container
we can scale easily. However, you have to write one proper health check to monitor
the health of all your microservices (Haven't thought about this)

### What is an API?
 It is a set of clearly defined communication to always access your microservice. **_e.g._**
 UBER started off using google maps when they first built their app. However due to costs,
 they switched to Mapbox (open-source) which is free. It was an easy switch for Uber
 to make. However, later on Google simplified its Maps API pricing and Uber could easily
 connect back to use it once they decided to.

### REST API
REST (representational state transfer) API has defined standard http methods:
 *  **GET, POST, PUT, DELETE**

### Fizzbuzz problem
Say Fizz when multiple of 3. Say Buzz multiple of 5. FizzBuzz multiple of both 3 and 5.
We make this an API which we can pass integers to and get the result returned to us
through the __GET__ method.


### Test driven development approach
It is good to approach this with a software cycle focused on **_testing_**. Cycle follows:
1. Create git repo
2. Setup repo locally
3. TDD - test driven development - unit tests (start with a fail test)
4. Business logic implementation - acceptance criteria.
5. REST API
6. Build router controller
7. End-to-end integration (check with curl or postman)
8. Commit local changes to github.

#### 2. Setup repo locally
```zsh
$ mkdir first_flask_project
$ cd first_flask_project
$ pip install virtualenv
$ virtualenv venv --python=python3.7
$ source venv/bin/activate
$ pip install Flask
$ pip install Flask-RESTful
$ pip freeze > .\requirements.txt
$ deactivate
$
```

#### 3. TDD - test driven development - unit tests
According to TDD -> RED-GREEN-BLUE. Fail our unit test first, then implement our
 business case depending on criteria. We fail it at the beginning. As a developer (we
 do so much copy and pasting that we don't want to copy and assume anything works. Start
 off from failure and build from there) then by doing RGB, we will be sure our methods
 work when they eventually pass. Unit testing in **fizzbuzz_service_spec.py**.
```python
import unittestfrom fizzbuzz_service import FizzBuzzService

class FizzBuzzServiceTest(unittest.TestCase):
    def test_firsttest(self):
        self.assertEqual('fail', FizzBuzzService.validate(32))

```

#### 4. Business logic implementation - acceptance criteria.
Write this in a file called **fizzbuzz_service.py** file, outlining the FizzBuzz logic.
Testing is performed by adding more unittests to **fizzbuzz_service_spec.py**.

#### 5. REST API
Make the REST API in the **app.py** file. Add a resource at a location and port 5000.
```python
app = Flask(__name__)
api = Api(app)
api.add_resource(FizzBuzzController, '/fizzbuzz/validate/<int:input_variable>')
app.run(port=5000, debug=True)

```

#### 6. Build router controller
Controllers are routers and define how to deal with incoming requests. The http get method
must be defined.
```python
from flask_restful import Resource
from fizzbuzz_service import FizzBuzzService

class FizzBuzzController(Resource):
    def get(self, input_variable):
        return FizzBuzzService.validate(input_variable)
```

#### 7. End-to-end integration (check with curl or postman)
Run the API locally.
```python
python app.py
```
You get the following message
```zsh
* Running on http://127.0.0.1:5000/
```
##### Check end-to-end integration with command line.
```zsh
curl --location --request GET 'http://127.0.0.1:5000/fizzbuzz/validate/96'
```
Returns Fizz.
##### Check end-to-end integration with Postman
Running Postman off the desktop client and making a GET request at:
`http://127.0.0.1:5000/fizzbuzz/validate/<number>` will return the request.

#### 8. Commit local changes to github (initialising repo locally)
```zsh
$ git init
$ git add .
$ git commit -m "First push to github"
$ git remote add origin https://github.com/comaraDOTcom/flask-demo.git
$ git push -u origin master
```

To install the atom packages on a new machine run
```zsh
$ apm install --packages-file ~/.atom/package.list
```
