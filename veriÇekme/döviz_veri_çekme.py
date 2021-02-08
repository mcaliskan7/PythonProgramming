import requests
import sys

currency = input("Currency: ")
value = float(input("Enter the value: "))

url = "http://data.fixer.io/api/latest?access_key=0a251f77bc5006fb4666ed21253134e4"
response = requests.get(url)

json_data = response.json()
try:
    print(json_data["rates"][currency] * value)
except KeyError:
    sys.stderr.write("Enter a valid currency.")
    sys.stderr.flush()


"CONVERT EURO TO OTHER CURRENCIES"
