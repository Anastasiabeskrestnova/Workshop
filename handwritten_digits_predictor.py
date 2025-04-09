from sklearn import datasets
from sklearn.neural_network import MLPClassifier

TRAIN_SIZE = 1000
TEST_SIZE = 1000
def check_accuracy(predictions, labels):
    correct_predicitons = 0
    for index in range(len(predictions)):
        if predictions[index] == labels[index]:
            correct_predicitons += 1

    print(correct_predicitons/len(predictions))


digits_dataset = datasets.load_digits()
digit_labels = digits_dataset.target
digits_dataset = digits_dataset.images.reshape(len(digits_dataset.images), -1)

mlp = MLPClassifier(hidden_layer_sizes=(15),
                    activation='logistic',
                    alpha=1e-4, solver='sgd',
                    tol=1e-4, random_state=1,
                    learning_rate_init=.1,
                    verbose=False)


mlp.fit(digits_dataset[:TRAIN_SIZE], digit_labels[:TRAIN_SIZE])

predictions = mlp.predict(digits_dataset[TRAIN_SIZE:TRAIN_SIZE + TEST_SIZE])

check_accuracy(predictions, digit_labels[TRAIN_SIZE:TRAIN_SIZE + TEST_SIZE])
