## Repo based off Meetup by Rasim Sen
I attended a Meetup on RestAPI development with Python and Flask given by Rasim Sen on Zoom
on 19/10/2020.  

For an application, there are two possible architectures:

**Monolithic architecture:** (3 layer pattern - presentation/ui (front end), business
layer(implementing business logic), data access layer (database).
we are creating one monolith in one big bucket. It is not a good practice to directly 
connect the fronted to backend. i.e. big bucket that contains all the components.
**_For example_** on the on the backend we require more optimisation for performance
(not needed for the front end).


**Microservice architecture:** splits the backend into many smaller components. On the
backend side we prefer not to have all components in the same folder ( _i.e._** 
user_profile, shopping cart etc) because each component has different dynamics. But it
appears like they are together on the frontend..However on the back end, how it may work like so:
  * _search component_** might use elasticsearch as framework
  * _shopping cart_** might use NoSQL database

Each microservice can have a different framework and different technology. Another 
advantage is scalablility. If we were to put the app in a  kubernetes container
we can scale easily. However, you have to write one proper health check to monitor
the health of all your microservices (Haven't thought about this)

###What is an API?
 It is a set of clearly defined communication to always access your microservice. **__e.g._**
 UBER started off using google maps when they first built their app. However due to costs,
 they switched to Mapbox (open-source) which is free). It was an easy switch for Uber
 to make. However, later on Google simplified its Maps API pricing and Uber could easily
 connect back to use it once they decided to.
 
### REST API
REST (representational state transfer) API has defined standard http methods:  
  * GET
  * POST
  * PUT 
  * DELETE (HTTP methods).

### Fizzbuzz problem
Say Fizz when multiple of 3. Say Buzz multiple of 5. FizzBuzz multiple of both 3 and 5.
We make this an API which we can pass integers to and get the result returned to us
through the __GET__ method.


### Test driven development approach
It is good to approach this with a software cycle focused on testing. Cycle follows:
1. Create git repo
2. Setup repo locally
3. tdd - test driven development - unit tests (start with a fail test)
4. Business logic implementation - acceptance criteria.
5. REST API
6. Build router controller
7. End-to-end integration (check with curl or postman)
8. Commit local changes to github.