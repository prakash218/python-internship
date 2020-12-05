import json

myjsonfile = open(r'Day 12.json','r')

jsondata = json.load(myjsonfile)

print(jsondata)

myjsonfile.close()

"""
Output:

{'name': 'Prakash', 'age': 19, 'Student': True, 'Department': 'Computer Science', 'Percentage': 97.6, 'Arrears': None, 
'Course': {'Course ID': 1001, 'Subject': 'Operating system', 'Credits': 4}, 
'Hobbies': ['Speed cubing', 'Programming', 'Movies', 'Fitness']}


"""
"""
#created a .json file with the info given below
{
  "name": "Prakash",
  "age": 19,
  "Student": true,
  "Department": "Computer Science",
  "Percentage": 97.6,
  "Arrears": null,
  "Course": {"Course ID": 1001, "Subject": "Operating system", "Credits": 4},
  "Hobbies": ["Speed cubing","Programming","Movies","Fitness"]

}
"""