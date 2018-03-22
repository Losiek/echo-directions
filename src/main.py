# This is main file of program echo-directions
from client import Client
from directions import directions
from simple_web_server import run_server
import json

def load_settings(settings_file):
    with open(settings_file) as data_file:
        settings_parsed = json.load(data_file)
    return settings_parsed['api_key'], settings_parsed['origin'], settings_parsed['dest'],


if __name__ == "__main__":
    # Parse settings file
    api_key, origin, dest = load_settings("../settings.json")

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

    # Run server
    from sys import argv

    if len(argv) == 2:
        run_server(port=int(argv[1]))
    else:
        run_server()