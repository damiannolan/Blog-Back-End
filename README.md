# RESTful API - Python, Flask and MongoDB

Currently only acts as an endpoint that connects to a mongodb collection with basic functionality for HTTP Requests made using [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS)

Used as a Back End for a 3rd Year Undergraduate project in Data Representation and Querying.

This applications intends to be used in conjunction with a Front End Blogging Application which can 
be found [Here!](https://github.com/seantking/Blog-Front-End)

### Team
- Sean King
- Damian Nolan

## Getting Started

1. Clone
			
			git clone https://github.com/seantking/Blog-back-end.git

2. Ensure that Pymongo is installed
			
			python -m pip install pymongo

3. Start MongoDB

			mongod

4. Start the application

			python app.py

## Architecture

This applications runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) framework and [MongoDB](https://www.mongodb.com/) as a database.

### References

https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask