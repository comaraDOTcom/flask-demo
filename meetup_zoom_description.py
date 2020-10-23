# ****RESTAPI development with python and flask 19/10/2020****

# Name: Rasim SEN.
# Blockchain developer - AWS certified cloud
# Zero2hero - run a lot of java and javascript trainings and events. Useful for
# frontend, backend and fullstack. He can give advice on career paths and full training.

# RESTAPI development with python and flask 19/10/2020

"""
Monolithic architecture (3 layer pattern - presentation/ui (front end), business layer(implementing business logic), data access layer (database).
we are creating one monolith in one big bucket. From the front it is not a good practice to connect directly to backend. i.e. big bucket that keeps everything.
But on the backend we require more optimisation for performance.


Microservice architecture: split backend into many smaller components. In the backend side we prefer not to have all components in the same folder (user_profile, shopping cart etc) because each component has differen
dynamics. But it appears like they are together on the frontend..
However on the bag end, search component might use elasticsearch as framework, shopping_cart might use NoSQL database...each microservice can have a different framework and different technology.
Another advantage is scalablility. If we put it in a kubernetes container we can scale easily.
However, you have to right one proper health check to monitor the health of all your microservices.

What is an API. It is a set of clearly defined communication to always access your microservice. e.g. UBER started off using google maps (however switched to OS mapbox is free). Easy switch for Uber to make.
However, Google simplified its Maps API pricing and Uber could easily connect back.

REST (representational state transfer) API - standard methods
GET POST PUT DELETE (HTTP methods).
Different cases when to use them.
"""


#FizzBuzz problem.
"""
Say Fizz when multiple of 3
Say Buzz multiple of 5
FizzBuzz multiple of both 3 and 5.
"""

#Approach 1. Implement business logic
#2. Add into
#3. Call it.

#Software cycle
"""
1. git repo
2. setup repo locally
3. tdd - test driven development - unit tests
4. business logic implementation - acceptance criteria.
5. REST API
6. router controller
7. end-to-end integration
8. commit local changes to github.
"""

# 1. make a new repo in github.
# 2. make local folder (makes a virtual env locally) where we pip install flask-RESTful.
# 3. we do some sort've source venv/bin/activate
# 4. open project in pycharm.


