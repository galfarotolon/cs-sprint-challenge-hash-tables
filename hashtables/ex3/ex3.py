def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # cache to keep track of values
    cache = {}

    # result stores values that have been repeated
    # in all of the lists 
    result=[]

    for i in arrays[0]:
        # hard code first value to 1 
        # as it is the first time added to the cache
        # key: digit, value: 1
        cache[i] = 1

    for i in range(len(arrays) - 1):
        
        #check the remaining arrays and compare them with
        # the first array, stored in cache already
        for j in arrays[i+1]:
            # check the second list one digit at a time, only store in cache if 
            # value has been repeated i.e. value increases from 1 to 2

            if j in cache:
                # increase value by 1 if digit is repeated
                cache[j] +=1
    
    
    
    for i in cache:
        # match the amount of repeated values to the number of arrays
        # being checked. i.e.:

        # if there are 3 arrays, repeated value must be 3,
        # if there are 250 arrays, repeated value must be 250
        # in order to append to the result, to make sure
        # the values have been repeated in ALL of the arrays
        if cache[i] == len(arrays):
            result.append(i)
        

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
