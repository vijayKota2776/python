#Python script to sort (ascending and descending) a dictionary by value.
d={"value1":"key1","value2":"key2","value3":"key3","value4":"key4"}
print("The dictonary in assending order by values",sorted(d.items(), key=lambda item: item[1]))
print("The dictonary in descending order by values",dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))

#program to remove duplicates from the dictionary. 
d={"value1":"key1","value2":"key2","value3":"key3","value4":"key4","value1":"key1","value2":"key2"}
unique_dict = {}
for k, v in d.items():
    if v not in unique_dict.values():
        unique_dict[k] = v
print(unique_dict)

#program to combine two dictionary by adding values for common keys
def combine_dicts(dict1, dict2):
    combined_dict = {k: dict1.get(k, 0) + dict2.get(k, 0) for k in set(dict1) | set(dict2)}
    return combined_dict


dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {2: 5, 3: 15, 4: 25}
result = combine_dicts(dict1, dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Combined Dictionary:", result)

#program to create a dictionary from a string
str=input("enter string")
d={}
for i in str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

#Here's a Python program to match key-value pairs in two dictionaries:
def match_key_value(dict1, dict2):
    matched_pairs = {k: v for k, v in dict1.items() if k in dict2 and dict2[k] == v}
    return matched_pairs
dict1 = {1: "a", 2: "b", 3: "c", 4: "d"}
dict2 = {1: "a", 2: "x", 3: "c", 5: "e"}
matched_pairs = match_key_value(dict1, dict2)
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Matched Key-Value Pairs:", matched_pairs)
