from numpy import exp, array, random, dot

class NeuralNetwork():

    def __init__(self):
        #Seeding to match the value with Siraj
        random.seed(1)

        #Assign random values to the 3 x 1 matrix within the range of -1 to 1 and mean 0
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    def __sigmoid(self, x):
        """Defining the activation function"""
        return 1 / (1 + exp(-x))

    #Gradient of sigmoc curve
    def __sigmoid_derivative(self, x):
        """Derivative of the sigmoid function"""
        return x * (1 - x)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        """ """
        for iterations in range(number_of_training_iterations):
            #Pass the training set through neural net
            output = self.predict(training_set_inputs)

            #Calculate the error
            error = training_set_outputs - output

            #Multiply the error by input and by gradient of sigmoid curve
            adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

            #Adjust weights
            self.synaptic_weights += adjustment

    def predict(self, inputs):
        """Pass inputs through our neural network""" 
        return self.__sigmoid(dot(inputs, self.synaptic_weights)) 

if __name__ == "__main__":

    #Initializing a single Neural Network
    neural_network = NeuralNetwork()

    print("Random starting synaptic weights")
    print(neural_network.synaptic_weights)

    #The training set has four values of all one's and zeros
    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    #Train the neural network 10,000 times and make small adjustments each time
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("New Synaptic weights after training")
    print(neural_network.synaptic_weights)

    print("Test Neural Network")
    print(neural_network.predict(array([1, 0, 0])))
