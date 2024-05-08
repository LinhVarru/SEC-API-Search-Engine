import requests
import json
api_url = "https://data.sec.gov/submissions/CIK0000704172.json"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'}

def getAPI():
    response = requests.get(api_url, headers=headers)
    data_text = response.text
    data = json.loads(data_text)
    json_object = json.dumps(data, indent=4)
    ExportToJson(json_object)
def ExportToJson(data):
    with open("sample1.json", "w") as outfile:
        outfile.write(data)

getAPI()