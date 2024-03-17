###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # open file
    cow_file = open(filename, 'r')
    cow_dict = {}
    for line in cow_file:
        # each line only has name and weight, separated by ','
        line = line.split(',')
        cow_dict[line[0]] = int(line[1])
    return cow_dict            
    

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # create a small function that also uses recursion but for each trip
    def each_trip(cows2, limit2=10):
        max_weight = 0
        max_cow = False
        for cow in cows2:
            # find the heaviest cow that is still under limit 
            if cows2[cow] < limit2 and cows2[cow] > max_weight:
                # update the current heaviest cow and its weight
                max_cow = cow
                max_weight = cows2[max_cow]
        # base case is if there are no cows that weight less than the limit
        if max_cow == False:
            return []
        # recursive call with a reduced list and reduced weight limit
        else:
            # calculate new limit before popping max cw from cows
            new_limit = limit2 - cows2[max_cow]
            cows2.pop(max_cow) # notice that this will pop cows from the original dict 
            return [max_cow] + each_trip(cows2, new_limit) # so the cows2 dict is updated
    
    # the big function uses recursion to get each trip from the small function
    # base case is if there is no cow left
    if len(cows) == 0:
        return []
    else:
        this_trip = each_trip(cows, limit) 
        # the each_trip function not only return a cow list but also pop thos cows from the original dict
        return [this_trip] + greedy_cow_transport(cows, limit) # so we can just use the updated cows dict

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    current_lst = []
    best_lst = []
    for partition in get_partitions(cows): # get each partition
        current_lst = []            # reset current list
        for lst in partition:       # each list in a partition
            weight = 0              # for acumulating the weight of cows in the list
            for cow in lst:         # acumulate
                weight += cows[cow]
            if weight > limit:      # if the accumulated weight > limit
                current_lst = []    # empty the return list 
                break               # and break out the for loop since the current partition is invalid
            else:                   # else we add the current cow list into the return list
                current_lst += [lst]# if succeed for all lists in a partition, the return list will be the same as the current partition
        if current_lst != []:       # if the return list is not empty, that means it succesfully copied the last partition
            if best_lst == []:      # check if best list is empty
                best_lst = current_lst
            elif len(best_lst) > len(current_lst): # if best list is not empty and longer than current list, update best list
                best_lst = current_lst
    return best_lst
    
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cow_data = load_cows('ps1_cow_data.txt')
    print(cow_data)
    
    start = time.time()
    trips_1 = greedy_cow_transport(cow_data, 10)
    end = time.time()
    print(end - start)
    print(len(trips_1))
    print(trips_1)
    
    #--------------------------------------------
    # need to load cow data again since the 1st method pop cows from dict
    cow_data = load_cows('ps1_cow_data.txt')
    start = time.time()
    trips_2 = brute_force_cow_transport(cow_data, 10)
    end = time.time()
    print(end - start)
    print(len(trips_2))
    print(trips_2)


if __name__ == '__main__':
    compare_cow_transport_algorithms()
