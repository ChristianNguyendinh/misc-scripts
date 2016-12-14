import requests, json

# classes to get data for
list_of_classes = ['cmsc131', 'cmsc132']

# TODO: see if can get more specific data for these classes

# Very simply downloads class data from the umd api (http://umd.io/)
# and stores it in a json file
# Requires requests to be installed


for course in list_of_classes:
	file_name = course + "_data.json"
	#print(file_name)
	f = open(file_name, 'w')
	url = 'http://api.umd.io/v0/courses/' + course + '?expand=sections'
	#print(url)
	r = requests.get(url)
	#print(json.dumps(r.json(), indent=4))
	
	f.write(json.dumps(r.json(), indent=4))
	f.close()
