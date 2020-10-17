import requests
from Constants import BASE


def Demo():
	#Sample list of sources and destination
	data = [
	{"src":"13.388860,52.517037","dst": ["13.397634,52.529407","13.428555,52.523219"]},
	{"src":"13.388860,52.517037","dst": "13.397634,52.529407"},
	{"src":"13.388860,52.517037","dst": ["13.397634,52.529407","13.428555,52.523219","47.4979,19.0402"]}
	]

	# Make a GET request with each of the values in the list
	for i in range(len(data)):
		response = requests.get(BASE, data[i])
		print(response.json())

	# To be able to visualize the responses from our request
	input()

if __name__ == "__main__":
	Demo()