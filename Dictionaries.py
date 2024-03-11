'''A dictionary is a built-in data type used to store key-value pairs. 
It is mutable, unordered, and indexed.'''

#dict has no indexing
#dict is mutable
#keys should always be immutable, values can be mutable
#keys should be unique,Dictionaries cannot have two items with the same key

#empty
dict = {}
print(dict)

dict1 = {"Name":"Bhakti", "age":26}
print(dict1)

dict2 = {"Nao" : "Bhakti"}
print(dict2)

#nested
person = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'zipcode': '12345'
    }
}

#accessing items, need to use keys always , no indexing
print(person['name'])  # Output: John
print(person['address']['city'])  # Output: Anytown

print(person.keys())
print(person.values())

#edit dict
person['name'] = 'Bhakti'
print(person)

#add new key-value pairs
print(dict1)
dict1['City'] = "Pune"
print(dict1)

#delete
del dict1['City']
print(dict1)

#del dict1 #delete whole dictionary
#print(dict1)

dict1.clear()
print(dict1)