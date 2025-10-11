# Applied mathematics: Outcome 3 - bitwise

# function to demonstrate usage of bitwise operators
def bitwise_samples(a = 56, b = 14):
    # print out the starting values
    print("a=",a,":", bin(a), "b=",b,":", bin(b))

    # initialise c to 0
    c = 0

    # TODO c = bitwise AND of a and b
     print("Result of a AND b is",c,":", bin(c))

    # TODO c = bitwise OR of a and b
    print("Result of a OR b is",c,":", bin(c))

    # TODO c = bitwise XOR of a and b
    print("Result of a XOR b is",c,":", bin(c))

# test the functions
bitwise_samples()
