def display(array):
    """
        Display an array using comma 

        Usefull when using NetVis to visualize the network :
        allows us to copy the array into a list for NetVis

        eg :
        [
            [0, 1],
            [5, 6]
        ]
        instead of :
        [[0 1]
         [5 6]]
    """

    L=[list(i) for i in array]
    print("[\n    ", end="")
    print(*L, sep=",\n    ")
    print("]")   