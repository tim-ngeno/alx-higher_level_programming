# 0x11. Python - Network #1

## Using urllib

### Fetching Internet Resources

```python
import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)
content = response.read()
```

### Decoding urllib Body Response

```python
decoded_content = content.decode('utf-8')
```

## Using requests

> Note: requests is way simpler than urllib!

### Installing requests

```bash
pip install requests
```

### Making an HTTP GET Request

```python
import requests

response = requests.get("https://www.example.com")
content = response.text
```

### Making an HTTP POST/PUT/etc. Request

```python
# POST
response = requests.post("https://www.example.com", data={"key": "value"})

# PUT
response = requests.put("https://www.example.com", data={"key": "value"})
```

### Fetching JSON Resources

```python
response = requests.get("https://api.example.com/data")
json_data = response.json()
```

### Manipulating Data from an External Service

```python
title = json_data['title']
```

## Sending Headers with a Request

When interacting with web services, you often need to send specific headers (e.g., user-agent, authentication tokens).

```python
headers = {
    "User-Agent": "MyApp/0.0.1",
    "Authorization": "Bearer YOUR_TOKEN_HERE"
}
response = requests.get("https://api.example.com/data", headers=headers)
```

### Passing URL Parameters

You might need to send some URL parameters for GET requests:

```python
params = {
    "query": "Python",
    "count": 10
}
response = requests.get("https://api.example.com/search", params=params)
```

### Handling Response Status

After making a request, it's a good practice to check if the request was successful:

```python
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    print("Success!")
else:
    print(f"Failed with status code: {response.status_code}")
```

### Handling Timeouts

When making requests, your script might hang indefinitely if the server doesn't respond. To avoid this, set timeouts:

```python
try:
    response = requests.get("https://api.example.com/data", timeout=5)  # 5 seconds timeout
except requests.Timeout:
    print("The request timed out")
```

### Using Sessions

If you're making multiple requests to the same host, using a Session can speed things up:

```python
with requests.Session() as session:
    response1 = session.get("https://api.example.com/data1")
    response2 = session.get("https://api.example.com/data2")
```

### Error Handling

Always be prepared for potential errors:

```python
response = requests.get("https://api.example.com/data")
try:
    response.raise_for_status()  # This will raise an exception for 4xx and 5xx status codes
except requests.RequestException as error:
    print(f"An error occurred: {error}")
```
