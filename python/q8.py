'''8.	Develop a program to sort a list of dictionaries by a specific key.'''

def sort_dicts_by_key(dicts, key):
    try:
        key_arr = [dict_ele[key] for dict_ele in dicts]
        key_arr.sort()
        return [dict_ele for num in key_arr for dict_ele in dicts if num == dict_ele[key]]
        # alternate:: return sorted(dicts, key=lambda x: x[key])
    except Exception as e:
        print(e)

if __name__=="__main__":

    data = [
        {"name": "raju", "age": 25},
        {"name": "rahul", "age": 30},
        {"name": "rajat", "age": 20}
    ]

    sorted_data = sort_dicts_by_key(data, "age")
    print("Sorted by age:", sorted_data)
    
    sorted_data = sort_dicts_by_key(data, "name")
    print("Sorted by name:", sorted_data)
