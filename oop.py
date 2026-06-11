# OOP - Object-Oriented Programming
# request(so'rov) - response(javob)
# JSON (JavaScript Object Notation) - ma'lumotlarni almashish formati
# HTTP / HTTPS - HyperText Transfer Protocol / Secure
# 1. GET(data olish)
# 2. POST(data yuborish)
import requests

# Make a request
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
# print(response.status_code)
# Get data as JSON
data = response.json()
print(data)
