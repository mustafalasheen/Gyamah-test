import requests
import json

# Create a new user
user_data = {
    "id": 123,
    "username": "lasheen",
    "firstName": "Test",
    "lastName": "User",
    "email": "lasheeen@gmail.com",
    "password": "pa55word123",
    "phone": "01004901795"
}

# Create user
create_response = requests.post(
    "https://petstore.swagger.io/v2/user",
    json=user_data
)
print("User creation status:", create_response.status_code)

# Get user information
get_response = requests.get(f"https://petstore.swagger.io/v2/user/lasheen")
if get_response.status_code == 200:
    user_info = get_response.json()
    print("User email:", user_info.get('email'))
else:
    print("Failed to retrieve user information")