from math import floor
def find_pos(thread, sim_size = [100, 100, 100]):
    x = thread % sim_size[0]
    y = int((thread - x)/sim_size[1] % sim_size[1])
    z = int(thread / (sim_size[0] * sim_size[1]))

    print("Thread: {}".format(thread))
    print("X position: {}" .format(x))
    print("Y position: {}".format(y))
    print("Z position: {}".format(z))
    #print("\n")

    #


def find_neighbors(thread, sim_size = [4, 9, 5]):
    for z in range(-sim_size[2] * sim_size[1], (sim_size[1] * sim_size[2])+1, sim_size[2]*sim_size[1]):
        for y in range(-sim_size[1], sim_size[1]+1, sim_size[1]):
            for x in range(-1, 2, 1):
                #print(y)
                #print(x)
                print(thread + z + y + x)
                #print('\n')




#import numpy as np
#vec_find_pos = np.vectorize(find_pos)
#vec_find_pos(np.arange(100))
