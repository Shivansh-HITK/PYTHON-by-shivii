TOPIC 1: JSON (JavaScript Object Notation)
yeh backend ka language hota hai
it looks very similar to python dict but it is not same as python dict
format : string
we need to import json

from string.templatelib import convert module to work with json data in python

import json

# Python Dictionary (Humara data)
student = {
    "name": "Rahul",
    "course": "Backend",
    "marks": 95
}

# 1. Python Dict -> JSON String (Yeh hum frontend par bhejenge)
# 'indent=4' se JSON aakhne mein suddha lagta hai (pretty print)
json_string = json.dumps(student, indent=4)  IMP : dumbs ka matlb python me hota hai to convert python dict to json string, aur loads ka matlab hota hai json string ko python dict me convert karna.
print("Yeh JSON hai jo bhejenge:\n", json_string)
print(type(json_string)) # Output: <class 'str'>

# 2. JSON String -> Python Dict (Jab frontend se data aaye)
received_json = '{"username": "Priya", "is_admin": false}'
# JSON mein 'true/false' hota hai, Python mein 'True/False'
parsed_data = json.loads(received_json) 
print(parsed_data["username"]) # Output: Priya
print(type(parsed_data))       # Output: <class 'dict'>