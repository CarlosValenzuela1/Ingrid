import requests
from constants import *

def Main():
    list_of_dst = []
    src = "13.388860,52.517037"
    list_of_dst.append("13.397634,52.529407")
    list_of_dst.append("13.428555,52.523219")
    routes = prepare_routes(src, list_of_dst)

    resp_dict = {}
    resp_dict[SOURCE] = src
    resp_dict[ROUTES] = routes
    print(f"Dictionary: {resp_dict}") 

def prepare_routes(src, list_of_dst):
        routes = []
        for dst in list_of_dst:
            route_details = {}

            # This will get any route field we want from OSRM API
            fields = get_fields(src, dst)

            # Using constants to deal with OSRM API fields
            route_details[DESINTATION] = dst            
            route_details[DURATION] = fields[DURATION]
            route_details[DISTANCE] = fields[DISTANCE]
            routes.append(route_details)
        return routes

def get_fields(src, dst):
    resp = requests.get("http://router.project-osrm.org/route/v1/driving/" + src + ";" + dst + "?overview=false")
    resp_dict = resp.json()
    fields = resp_dict[ROUTES][0]
    return fields



if __name__ == "__main__":
	Main()