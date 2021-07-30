from ipstack import GeoLookup
import requests
from functions import bcolors
import json
from tabulate import tabulate


geo_lookup = GeoLookup("df6408ba60040d3916544f85e5f0717d")
API_KEY = "df6408ba60040d3916544f85e5f0717d"



def ipstack_API():

	ip = input(f"{bcolors.OKGREEN}Ingresa una direccion IP: {bcolors.ENDC}")
	temp_table = []
	table = []
	try:
	    # Retrieve the location information for 
	    # github.com by using it's hostname.
	    # 
	    # This function will work with hostnames
	    # or IP addresses.
	    location = geo_lookup.get_location(ip)

	    for item in location:
	    	temp_table.append(item)
	    	temp_table.append(location[item])
	    	table.append(temp_table)
	    	temp_table = []
	    table.pop()
	    # If we are unable to retrieve the location information
	    # for an IP address, null will be returned.
	    if location is None:
	        print("Failed to find location.")
	  
	    return(table)
	except Exception as e:
	    print(e)




def ipapi_API():
	ip = input(f"{bcolors.OKGREEN}Ingresa una direccion IP: {bcolors.ENDC}")
	temp_table = []
	table = []
	try:


	    r = requests.get("https://ipapi.co/" + ip + "/json")
	    for item in r.json():
	    	temp_table.append(item)
	    	temp_table.append(r.json()[item])
	    	table.append(temp_table)
	    	temp_table = []
	
		
	    return table
	except Exception as e:
	    print(e)






