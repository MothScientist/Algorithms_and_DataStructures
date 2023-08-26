def radix_sort(sorting_list):
    # find the size of the longest number
    max_digits = max([len(str(x)) for x in sorting_list])

    # radix
    base = 10

    # create an intermediate empty array of 10 elements
    bins = [[] for _ in range(base)]

    # iterate over all digits, starting from zero
    for i in range(0, max_digits):

        # iterate over all elements in an array
        for x in sorting_list:

            # get the digit on the current digit in each number of the array
            digit = (x // base ** i) % base

            # we send the number to the intermediate array in the cell that matches the value of this digit
            bins[digit].append(x)

        # collect all non-zero values from the intermediate array into the initial array
        sorting_list = [x for queue in bins for x in queue]

        # clear the intermediate array
        bins = [[] for _ in range(base)]

    return sorting_list