

# @app.route("/")
# def home():
# 		return render_template("index.html")

# @app.route("/new", methods=["POST"])
# def new_item():
# 	form_data = request.form
# 	print form_data
# 	print form_data["name"]
# 	print form_data["amount"]
# 	print form_data["category"]
# 	return "Item submitted!"

from flask import Flask, render_template, request

app = Flask("MyApp")

import datetime
now = datetime.datetime.now().date()

number = raw_input("How many items do you want to add?")
number = int(number)

items = {
}

for food in range(number):
	items[food] = {}
	items[food]["name"] = raw_input("What is it?")
	items[food]["amount"] = raw_input("How much do you have?") 
	items[food]["category"] = raw_input("What category is it?")
	items[food]["date"] = now

# print items

@app.route("/")
def home():
 		# print (items)
 		return "Item submitted!"

app.run(debug=True)