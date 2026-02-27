import json
person = '''{
"name" : "bibek",
"address":"nakhipot"


}'''
person_dict = json.loads(person)
print(person_dict['name'])
print(person_dict['address'])
person_dict['address'] = 'lalitput,nakhipot'
print(person_dict)
json_output = json.dumps(person_dict,indent=4)
print("\n modified json:")
print(json_output)