import numpy as np
x_input = np.array(([3,1.5],[2,1],[4,1.5],[3,1],[3.5,0.5],[2,0.5],[5.5,1],[1,1],[4,1.5]),dtype=float)
y = np.array (([1],[0],[1],[0],[1],[0],[1],[0]),dtype=float) # donnees de sortie 1 = Rouge / 0 = bleu

x_input = x_input/np.amax(x_input, axis=0)

X = np.split(x_input,[8])[0]
xPrediction = np.split(x_input,[8])[1]

class Neural_Network(object):
    def __init__(self):
        self.inputSize = 2
        self.outputSize=1
        self.hiddenSize = 3

        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # Matrice 2x3
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # Matrice 3x1

    def forward(self,X):

        self.z = np.dot(X,self.W1)
        self.z2 = self.sigmoid(self.z)
        self.z3 = np.dot(self.z2,self.W2)
        o = self.sigmoid(self.z3)
        return o
        
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self,s):
        return s * (1-s)
    def backward(self,X,y,o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.sigmoidPrime(o)

        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)

        self.W1 += X.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)
    def train(self,X,y):
        o = self.forward(X)
        self.backward(X,y,o)

    def predict(self):
        print("Donnée predite apres entrainement: ")
        print("Entree : \n" + str(xPrediction))
        print("Sortie : \n" + str(self.forward(xPrediction)))

        if(self.forward(xPrediction) <= 0.5):
            print("La fleur est BLEU ! \n")
        else:
            print("La fleur est ROUGE ! \n")


NN = Neural_Network()

for i in range(30000):
    print("#" + str(i) +"\n")
    print("Valeurs d'entrées: \n" + str(X))
    print("Sortie actuelle: \n" + str(y))
    print("Sortie predite: \n" + str(np.matrix.round(NN.forward(X),2)))
    print ("\n")
    NN.train(X,y)
NN.predict()