# Question no 1
# Write apython program that initializes an array with 5 numbers
# adds a nnew number to the array and prints the updated array
import array as arr
a=arr.array('i',[1,2,3,4,5])
print(a.tolist())
a.append(6)
print("updated list: ",a.tolist())

# Question no 2
# create a program that takes user input to add multiple elements to an array,then prints the final array
array=[]
numbers=input("Add your required numbers: ")
array.append(numbers)
print(" the resultant array is: ",array)

# Question no 3
# read a JSON file containing NASA APOD data and print specific keys
import json
json_data='''{
  "date": "2024-08-06",
  "explanation": "This is the explanation of atronomy picture of the day",
  "hdurl": "http://example.com/image_hd.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "Astronomy picture of the day",
  "url": "http://example.com/image.jpg
}'''
data=json.loads(json_data)
print("media_type:",data.get("media_type"))
print("Title:",data.get("title"))

# Question no 4
# use the requests module to send a GET request and print the JSON response
import requests
url='http://api.open-notify.org/iss-now.json'
response=requests.get(url)
print("JSON Rsponse: ",response.json())

# Question no 5
# print specific fields from the json response using requests
import requests
url='http://api.open-notify.org/iss-now.json'
response=requests.get(url)
data=response.json()
print("latitude:",data['iss_position']['latitude'])
print("longitude:",data['iss_position']['longitude'])

# Question no 6
# Write ISS location data to a csv file using pandas
import requests
import pandas as pd
from datetime import datetime
url='http://api.open-notify.org/iss-now.json'
arr=[]
for _ in range(100):
    response=requests.get(url)
    data=response.json()
    arr.append({
        'timestamp':datetime.fromtimestamp(data['timestamp']),
        'latitude' :data['iss_position']['latitude'],
        'longitude' :data['iss_position']['longitude']
    })
    df=pd.DataFrame(arr)
    df.to_csv('iss_location.csv',index=False)
    print("data written to 'iss location is")

