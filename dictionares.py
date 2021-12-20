person={'name':"May Thazin Htun",
        'age':"29"}
print(f'Person dictionary {person}');
print(f'Extract keyy from dictionay {person["name"]}');
person['hair_color']="Black";
print(f'Add to data dictionary {person}');
print(f'Use in keyword in data dictionary {"name" in person}');

if 'name' in person :
    print('work');
if 'skin' in person :
    print('work');

per_keys_dic_list=person.keys();
print(per_keys_dic_list);
per_keys=list(person.keys());
print(per_keys);
per_values=list(person.values());
print(per_values);