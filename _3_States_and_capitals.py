import json

# Dictionary of states and capitals
states_and_capitals = {
  "Andhra Pradesh": "Amaravati",
  "Karnataka": "Banglore",
  "Telangana":"Hyderabad",
  "Kerala":"Thiruvananthapuram",
  "Taminadu":"chennai",
  "Maharashtra": "Mumbai",
  "Madhya pradesh": "Bhopal",

}

# Open a file for writing
with open("states_capitals1.json", "w") as f:
  # Write the dictionary to the file in JSON format
  json.dump(states_and_capitals, f)

f = open(r"states_capitals1.json", "r")
print(f.read())