import requests

url = "https://app-dw6pp4uce-nuha-alansaris-projects.vercel.app/user"
payload = {
    "name": "John",
    "age": 30
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.status_code)
print(response.json())
