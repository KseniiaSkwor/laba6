dictionary = {"Россия": "Москва", "Франция": "Париж","Турция": "Анкара","Великобритания": "Лондон",}

print(dictionary)
print("Столица франции: ", dictionary["Франция"])

list_keys=list(dictionary.keys())
list_keys.sort()
for i in list_keys:
    print(i, ":", dictionary[i])
    
