


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

import datetime, requests

now = datetime.datetime.now().date()

# number = raw_input("How many items do you want to add?")
# number = int(number)

@app.route("/")
def home():
	return render_template("index.html")

items = {
	}

@app.route("/new", methods=["POST"])
def new_item():
	form_data = request.form
	print form_data
	print form_data["name"]
	print form_data["amount"]
	print form_data["category"]

	items["name"] = form_data["name"]
	items["amount"] = form_data["amount"]
	items["category"] = form_data["category"]
	items["date"] = now


	endpoint = "https://api.edamam.com/search"
	payload = {"q": items["name"], "app_id":"77a748cd", "app_key": "e0bf82dba0b0d85c32831026ee882210"}

	response = requests.get(endpoint, params=payload)

	print response.url
	print response.status_code
	print response.headers["content-type"]
	print response.json()

	list_urls = ""

	for recipe in response.json()["hits"][0:9]:
		list_urls += recipe["recipe"]["url"] + "\n"

	return list_urls

	# return "Item submitted: \n Name: {} \n Amount: {} \n Category: {} Date: {}".format(items["name"], items["amount"], items["category"], items["date"])

# for food in range(number):
# 	items[food] = {}
# 	items[food]["name"] = form_data["name"]
# 	items[food]["amount"] = form_data["amount"]
# 	items[food]["category"] = form_data["category"]
# 	items[food]["date"] = now

# print (items)



# @app.route("/")
# def home():
#  		# print (items)
#  		return "Item submitted: \n Name: {} \n Amount: {} \n Category: {} Date: {}".format(items[food]["name"], items[food]["amount"], items[food]["category"], items[food]["date"])



app.run(debug=True)








