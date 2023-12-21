import json
import requests

url = " http://0.0.0.0:10000/predict/"

input_data_for_model = {
    "title":"As U.S. budget fight looms, Republicans flip their fiscal script",
    "text":"NEW YORK/WASHINGTON (Reuters) - The new U.S. tax code targets high-tax states and may be unconstitutional, New York Governor Andrew Cuomo said on Thursday, saying that the bill may violate New York residentsâ€™ rights to due process and equal protection. ...",
    "subject": "politicsNews",
    "date": "December 31, 2017"
}

input_json = json.dumps(input_data_for_model)
response = requests.post(url, data=input_json)

# Handle the response
if response.status_code == 200:
    # Successful response
    json_output = response.json()
    json_output = json.loads(json_output)
    for k ,v in json_output.items():
        print(k,v)
else:
    # Error response
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.content)
