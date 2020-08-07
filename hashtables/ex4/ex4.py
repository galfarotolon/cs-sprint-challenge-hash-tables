def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # create cache to store all values for later
    cache = {}

    # store only the values with absolutes
    result = []

    # for each value in the array
    for val in a:
        # use absolute to check value
        if cache.get(abs(val)):
            # add value to the result array if its absolute
            result.append(abs(val))
        else:
            # if value is not there yet, add it to cache
            # to use later and reduce runtime
            cache[abs(val)] = val
        
      

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
