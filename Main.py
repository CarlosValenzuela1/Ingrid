import requests
import constants
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
from operator import itemgetter
from constants import DURATION, DISTANCE, DESTINATION, ROUTES, SOURCE

app = Flask(__name__)

@app.route("/")
def Main():
	src = request.args.get('src')
	list_of_dst = request.args.getlist('dst')
	if src == None:
		return {"status":"400", "message":"Please provide the coordinates for your source"}
	if len(list_of_dst) == 0:
		return {"status":"400", "message":"Please provide the coordinates for your destination"}
	print(f"What happened? {src} and {list_of_dst}")
	routes = prepare_routes(src, list_of_dst)

	if type(routes) is list:
		resp_dict = {}
		resp_dict[SOURCE] = src
		resp_dict[ROUTES] = routes
		#print(f"Dictionary: {resp_dict}")
		return resp_dict
	else:
		return routes

def prepare_routes(src, list_of_dst):
	""" Return the routes list which contains (destination, duration and distance) 
	The list is sorted by time and if two times are the same then by distance. """
	routes = []
	for dst in list_of_dst:
		route_details = {}

		# This will get any route field we want from OSRM API
		fields = get_fields(src, dst)
		if 'status' not in fields:
			# Using constants to deal with OSRM API fields
			route_details[DESTINATION] = dst
			route_details[DURATION] = fields[DURATION]
			route_details[DISTANCE] = fields[DISTANCE]
			routes.append(route_details)
		else:
			return fields

	# Only sort list if list is bigger than 1
	if len(routes) > 1:
		# This will only sort by duration
		sort_route_list_by_duration(routes)

		# Now that routes has been sorted, we will sort once more in case time (duration) is repeated
		sort_repetitions(routes)
	return routes

def get_fields(src, dst):
	""" Consumes the route service from OSRM API and returns all fields available.
		Details about OSRM API implementation can be seen here: 
		http://project-osrm.org/docs/v5.23.0/api/?language=cURL#route-service """
	try:
		resp = requests.get("http://router.project-osrm.org/route/v1/driving/" + src + ";" + dst + "?overview=false", timeout=30)
	# except timeout:
		# return {"status":"408", "message":"Unable to retrieve response from OSRM API the request timeout, please try again"}
	except requests.exceptions.RequestException as e:
		return {"status":"400", "message":"Connection to OSRM API was unsuccessful, please try again."}
		#raise SystemExit(e)
	
	if resp.status_code == 200:
		resp_dict = resp.json()
		fields = resp_dict[ROUTES][0]
		return fields
	else:
		return {"status":"400", "message":"Connection to OSRM API was unsuccessful, please try again."}

def sort_route_list_by_duration(list_):
	""" Sorts list using bubble sort algorithm by time (duration) """
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(list_) - 1):
			if list_[i][DURATION] > list_[i + 1][DURATION]:
				# We will swap both dictionaries
				list_[i], list_[i + 1] = list_[i + 1], list_[i]
				swapped = True

def sort_repetitions(list_):
	""" Sorts list using bubble sort algorithm by distance, only when there are duplicates in time. """ 
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(list_) - 1):
			if list_[i][DURATION] == list_[i + 1][DURATION]:
				if list_[i][DISTANCE] > list_[i + 1][DISTANCE]:
					# We will swap both dictionaries
					list_[i], list_[i + 1] = list_[i + 1], list_[i]
					swapped = True

if __name__ == "__main__":
	app.run(debug=True)
	#Main()
