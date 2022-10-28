import requests
response = requests.get('https://s3-eu-west-1.amazonaws.com/discovery-insure-interview-rev1/sightings_alerts.zip')
print(response)