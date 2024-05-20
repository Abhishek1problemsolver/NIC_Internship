def max_min_k_elements_in_tuple(input_tuple, k):
    if k > len(input_tuple) or k <= 0:
        print("Invalid value of k")
        return

    
    sorted_tuple = sorted(input_tuple)

    
    max_k_elements = sorted_tuple[-k:]

    
    min_k_elements = sorted_tuple[:k]

    return max_k_elements, min_k_elements


input_tuple = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

max_k, min_k = max_min_k_elements_in_tuple(input_tuple, k)
print(f"Maximum {k} elements of the tuple : {max_k}")
print(f"Minimum {k} elements of the tuple : {min_k}")
