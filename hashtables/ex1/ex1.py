cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    for key, value in enumerate(weights):
        cache[value] = key

    for key, w in enumerate(weights):
        if (limit- w) in cache:
            if cache[limit - w] > key:
                return(cache[limit -w ], key)
            else:
                return(key, cache[limit-w])
 
    return None
