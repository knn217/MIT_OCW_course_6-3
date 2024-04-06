def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    longest = 0
    length = 0
    for i in range(len(A)): # iterate through A 1 time, O(N)
        if i > 0 and A[i] > A[i-1]: # check if the elements are increasing
            length += 1 # keep track of increase length
        else:
            length = 0 # if not increasing, reset the length

        if length == longest: # every time length = longest, increase count by 1
            count += 1
        elif length > longest: # if length > longest, the previous count is meaningless, set count to 1 for the current longest
            count = 1
        longest = max(longest, length) # update longest each iter
    ##################
    return count
