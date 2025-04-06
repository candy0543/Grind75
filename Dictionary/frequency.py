def find_most_with_dict(arr):
    frequency = {}
    max_count = 0
    mode = []

    # Iterate through the array and count the frequency of each number
    # using a dictionary
    # and find the mode
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
        max_count = max(max_count, frequency[num])
    for num, count in frequency.items():
        if count == max_count:
            mode.append(num)

    return mode 

# Test the function
if __name__ == "__main__":
    arr = [1,1,2,3,4]
    print(find_most_with_dict(arr))
    
