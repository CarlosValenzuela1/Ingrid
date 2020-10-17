# Ingrid Backend Coding Task
# Applicant details:
- Name: Carlos Valenzuela
- Date: October 17, 2020
- Position: Junior Backend Engineer

# Note:
To be 100% honest I missread the technology section of the instructions and I attempted the coding task with my favorite language. I hope it still provides an insight to my capacities as a developer and apologies for the misunderstanding.

# How to run:
- Ensure you have python 3.6 or later installed
	- All the code should run fine in older python 3 versions except for the fstrings

- Assuming you have python 3 installed, simply navigate to the root of Ingrid directory with cmd and type: "python Main.py" (without quotations) 

- By executing Main.py, you will be running a Flask application
	- With this application you can run your own requests
	- App details:
		- HOST: http://127.0.0.1 
		- PORT: 5000

- You can also use Demo.py to use execute already existing requests

# Class Description:

- Main
	- This class contains the main logic of the Flask application
	- Methods:
		- Main: Defines the route to be used by the requests and kickstarts the whola application logic whenever a request.get is called to http://127.0.0.1:5000/

		- prepare_routes: Receives a source and a list of destinations. Returns a list containing details for the route of each destination received. Each destination will be its own dictionary containing the fields destination, duration, distance. This list will be sorted by time and in case of repited values, it will be sorted by distance

		- get_fields: Receives a source and a destination. It makes a route service request to OSRM API by providing the source and destination fields and it returns a dictionary of all the available fields. In case of failure, it returns an error message with the error code and message description of the failure

		- sort_route_list_by_duration: Receives a list of dictionaries. Each dictionary corresponds to the duration and distance between the source and destination. It sorts the list based on the duration value. The sort algorithm used is a simple bubble sort.

		- sort_repetitions: Receives a list of dictionaries. Each dictionary corresponds to the duration and distance between the source and destination. It case the list contains duplicates on its duration, then it sorts it by distance. The sort algorithm used is a bubble sort.

Demo
	- Contains a couple of simple GET requests to do a general demo of the API created.

Constants
	- Contains all the constants needed for Main, Demo and Unit_Test. This allows us to add/update any value without having to modify the code in case of future improvements

Unit_test
	- Contains a couple of helper methods I used while developing the application. The current state of Tests is simply for demonstration. It does not include tests for all the use cases, neither integration, regression or volume testing of the application. It was simply used as part of the TDD (Test-driven Development)

If you managed to read until here, then Thank you! and have a great day!