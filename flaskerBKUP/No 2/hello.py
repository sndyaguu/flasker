from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

#FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags

def index():
    first_name = "John"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41  ]
    return render_template("index.html", 
        first_name=first_name, 
        stuff=stuff,
        favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)