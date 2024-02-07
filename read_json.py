import json

with open('nyt_dec23.json') as user_file:
  parsed_json = json.load(user_file)

#json_obj = json.dumps(parsed_json)
# print the keys and values
for json_object in parsed_json:
 print("ttl: %s, desc: %s" % (json_object['title'],json_object['description']) )
