from flask import Flask                     # From the flask module import the flask class: Lowercase flask is the module. Class are "title case" - the first letter of every word is capitalized

app = Flask(__name__)                       # When you create an instance of a class, you get and object; app is now an object

@app.get("/")                               # Flask decorator that allows us to define routes
def home():
    me = {                                  # python3 dictionary
        "first_name": "Damian",
        "last_name": "Savage",
        "hobbies": "Motorcycles",
        "is_online": True
    }
    
    return me                               # When you return a dictionary from a flask view function, it's converted to JSON
