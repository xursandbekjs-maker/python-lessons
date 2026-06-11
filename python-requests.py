# API - Applicatin Programming Interface
# request - (so'rov) # response - (javob) 
# JSON (JavaScript Object Notation)
import requests

# Make a request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

# Print the response
print(response.json())