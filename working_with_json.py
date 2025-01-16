import json
'''
open a json file in r = read mode
then load the file 
finally print it
'''
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)

###########################

'''
to write a json file use w
json.dump ftn
'''
python_obj = {'name': 'John', 'age': 30}
with open('output.json', 'w') as file:
    json.dump(python_obj, file)

##### 

'''
for reading a large json file
increment it line by line
'''

with open('large_file.json', 'r') as file:
    for line in file:
        data = json.loads(line)
        # Process each line of JSON data    