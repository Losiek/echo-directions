# This is main file of program echo-directions
from client import Client
from directions import directions
import json

# Constans
settings_file = "../settings.json"

def load_settings(settings_file):
    with open(settings_file) as data_file:
        settings_parsed = json.load(data_file)
    return settings_parsed['api_key'], settings_parsed['origin'], settings_parsed['dest'],

api_key, origin, dest = load_settings(settings_file)

# Create client object
client = Client(key=api_key)

# Get response
rsp = directions(client, origin, dest,
               mode="transit", waypoints=None, alternatives=False, avoid=None,
               language=None, units="metric", region=None, departure_time=None,
               arrival_time=None, optimize_waypoints=False, transit_mode=None,
               transit_routing_preference=None, traffic_model=None)

parsed = json.loads(json.dumps(rsp, sort_keys=False, indent=4))[0]
print(json.dumps(parsed, sort_keys=False, indent=4))