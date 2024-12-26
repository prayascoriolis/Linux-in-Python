'''4.	Create a function to find the intersection of two lists.'''

def intersection_using_loops(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 5]
    list2 = [4, 5, 6, 7, 8, 5]
    print("Intersection using loops:", intersection_using_loops(list1, list2)) 
    # alternate solution: list(set(list1) & set(list2))
