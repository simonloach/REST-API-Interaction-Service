import requests
import argparse
import json
import re

parser = argparse.ArgumentParser()

parser.add_argument("mac", type=str, help="MAC Address in the format XX:XX:XX:XX:XX:XX")
args = parser.parse_args()

regex = re.match(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", args.mac)

if not regex:
    print("This is not a valid MAC Address")
    exit()

try:
    response = requests.get(f'https://api.macaddress.io/v1?apiKey=at_JfdgFtVlCEJBknc7EyDcXtvC0nWpM&output=json&search={args.mac}')
except requests.exceptions.RequestException:
    print("GET Request raised Error, please verify connection to https://macaddress.io")
    exit()

if response.status_code != 200:
    print(f"HTTP request returned not OK: {response.status_code}")
    exit()
json_data = json.loads(response.text)

if not json_data['macAddressDetails']['isValid']:
    raise ValueError('API response MAC Address not valid')


if 'vendorDetails' in json_data and 'companyName' in json_data['vendorDetails'] and json_data['vendorDetails']['companyName'] != '':
    print(json_data['vendorDetails']['companyName'])
else:
    print("Could not find company name in vendor details in the API response") 
