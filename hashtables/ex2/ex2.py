#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # empty array to append layovers
    route = []
    cache = {}

    for t in tickets:
        # print(t.source, t.destination)

        # set key value pairs
        # source is key, destination is value
        cache[t.source] = t.destination

    # initial ticket source is NONE
    curr_ticket = cache['NONE']

    # check all the layover flights/ when destination is not NONE
    while curr_ticket != 'NONE':
        #append the next flight
        route.append(curr_ticket)
        # update cache ticket source to tickets destination
        curr_ticket = cache[curr_ticket]


    # last append NONE to indicate end of route
    route.append('NONE')

    return route
