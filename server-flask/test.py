import requests
import json

response = requests.post('http://localhost:8000/process',
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps({'data':'Request'}))
print(response.json())