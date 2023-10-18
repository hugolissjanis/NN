import numpy as np

x1 = 3
x2 = 3
x3 = 4
x4 = 4
w1 = 2
w2 = 8
w3 = 7
w4 = 8
w5 = 4
w6 = 9
w7 = 3
w8 = 2
w9 = 5
w10 = 4
w11 = 4
w12 = 7
n1 = 0
n2 = 0
n3 = 0
b1 = 1


def ActivationFunc(a):
    print(a)

inputMatrix = [[x1],
          [x2],
          [x3],
          [x4]]



weightsFirstLayer = [[w1, w2, w3, w4],
                     [w5, w6, w7, w8],
                     [w9, w10, w11, w12]]

a = []
for i in range(0, len(weightsFirstLayer)):
    [unpack] = (np.dot(np.transpose(weightsFirstLayer[i]), inputMatrix))
    a.append(unpack + b1)  #unpackar yttre arrayen för att kunna lägga till biasen

ActivationFunc(a)
























































































# inputs = [x1, x2, x3, x4]
# weightsFirstLayer = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12]
# nodes = [n1, n2, n3]

# # Alla noder har ett värde
# for x in range(0, len(nodes)):
#     nodes[x] += b1
#     for i in range(len(inputs)):     
#         nodes[x] += (inputs[i] * weightsFirstLayer[(x+1)*len(inputs) - 1])

# inputMatrix = [[x1],
#           [x2],
#           [x3],
#           [x4]]

# weightMatrix = [[w1],
#                 [w2],
#                 [w3],
#                 [w4]]

# #transpose matrix
# inputsT = zip(*inputMatrix)

# print(inputsT * weightMatrix)







# Det ska vara matematiskt bevisat att två lager kan lösa alla prblem, jag måste hitta beviset