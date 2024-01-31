import json
import os

print("Enter word to search: ")
word_to_search = input().lower()

names = {}
directory = 'Actual Data'

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith(".json"):
            json_file = open(os.path.join(dirpath, filename))
            json_data = json.load(json_file)

            for i in json_data['messages']:
                if 'content' in i and 'sender_name' in i:
                    words = i['content'].lower().split()
                    if word_to_search in words:
                        if i['sender_name'] in names:
                            names[i['sender_name']] += 1
                        else:
                            names[i['sender_name']] = 1

            json_file.close()
            
print(names)