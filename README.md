# Base Structure of a Production Level FasAPI application

## Problem statement

FastAPI is a high performance, easy to learn, fast to code and ready for production python framework. It's easy to start a FastAPI project in a single file as we will see in Demo versions. 

```
from fastapi import FastAPI

app = FastAPI()

@app.route('/')
def index():
  return {'greeting': 'hello world!'}
 
```
FastAPI allows you to define your own file structure and this can be quite challenging, especially for newbies. That is where this repo comes in. `fastapi_structure` sets the scalfolding standard that you can adopt and be sure your application can scale without a problem. 

## File Structure

```tree
+-- fastapi_structure
|   +-- application/
|       +-- blog/
|           +-- __init__.py
|           +-- controller.py
|           +-- models.py
|           +-- routes.py
|           +-- schema.py
|       +-- session/
|           +-- __init__.py
|           +-- controller.py
|           +-- models.py
|           +-- routes.py
|           +-- schema.py
|       +-- utils/
|       +-- __init__.py
|       +-- config.py
|       +-- factory.py
|   +-- __init__.py
|   +-- main.py
```

In this file structure, we have two sub applciations, `blog` and `session`. These are so independent that they can be ported to another project with little or no change. In your own case, these may be called something else. The idea here is that each sub application has the exact same files:

- *__init__.py* : An init file, this can be an empty file, but it has to be present for python to interpret this folder as a module. 
- *controllers.py*: This is where you define your functions that actually perform specific tasks. 
- *models.py*: If you are using an ORM like [SQLAlchemcy](https://www.sqlalchemy.org/), then this is where you define the models for the specific module. 
- *routes.py*: You can as well call this `views.py` but I usually prefer `routes` because it makes it more explicit. Here you define your routes. Each route will call controller function to perfom the requested task. 
- *schema*: If you are using a serializer, this is where you will define your serializer models or classes. 


## Getting Started
To begin using this repo: 
1. Fork the repo, so you can have a copy of yoru own.
2. Clone the repo to you local development environment
3. Open your IDE and navigate to the folder to open the project
4. Create a virtual environment and install all dependencies found in requirements.txt
5. run `python main.py`

Start modifying as needed. If you encounter any difficulties, don't hesitate to open an issue. 

Happy Coding!! and happy FastAPI Life!
