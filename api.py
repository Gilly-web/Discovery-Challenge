#import requests
#response = requests.get('https://s3-eu-west-1.amazonaws.com/discovery-insure-interview-rev1/sightings_alerts.zip')
#print(response)
from urllib import request
import wget, zipfile, requests, csv, pandas as pd, seaborn as sns, numpy as np, matplotlib.pyplot as plt
from io import BytesIO

url = 'https://s3-eu-west-1.amazonaws.com/discovery-insure-interview-rev1/sightings_alerts.zip'

req = requests.get(url)
print('Download Complete')

myZipfile = zipfile.ZipFile(BytesIO(req.content))
myZipfile.extractall('Extracted')

myCsvFile = pd.read_csv('Extracted/sightings_alerts/4cb82c2383ad.csv')
#print(myCsvFile.head(10))


#myHeatMap = sns.load_dataset(myCsvFile)
myHeatMap = pd.pivot_table(data=myCsvFile, index='lat',columns='lon',values='acc')
print(myHeatMap)
sns.heatmap(myHeatMap, cmap="Blues")
plt.show()