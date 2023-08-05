def perform_set_operations(set1, set2):
    union_result = set1.union(set2)
    intersection_result = set1.intersection(set2)
    difference_result = set1.difference(set2)
    symmetric_difference_result = set1.symmetric_difference(set2)

    print("Union of E and N is", union_result)
    print("Intersection of E and N is", intersection_result)
    print("Difference of E and N is", difference_result)
    print("Symmetric difference of E and N is", symmetric_difference_result)

# Define two sets E and N
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

# Perform set operations on E and N
perform_set_operations(E, N)
