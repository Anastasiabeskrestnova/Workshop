from sklearn.neural_network import MLPClassifier
from numpy import asarray 
from PIL import Image, UnidentifiedImageError
from os import listdir
from random import shuffle

NASTYA_DOCS_PATH = "/Users/nastyabeskrestnova/Documents/"

def unite_pairs(dataset, labels):
    united_pairs = []
    for index in range(len(labels)):
        pair = dataset[index], labels[index]
        united_pairs.append(pair)

    return united_pairs


def prepare_images_format(label, labels):
    dataset = sorted(listdir(NASTYA_DOCS_PATH + label))
    prepared_dataset = []

    for img_name in dataset:
        try:
            prepared_dataset.append(asarray(Image.open(NASTYA_DOCS_PATH + label + "/" + img_name).convert("RGB")).flatten())
            labels.append(label)
        except UnidentifiedImageError:
                continue

    return prepared_dataset


def divide_pair(pairs, labels):
    divided_dataset = []
    for pair in pairs:
        divided_dataset.append(pair[0])
        labels.append(pair[1])

    return divided_dataset


def check_accuracy(predictions, labels):
    labels = trim_endings(labels)
    correct_predicitons = 0
    for index in range(len(predictions)):
        if predictions[index] == labels[index]:
            correct_predicitons += 1

    print(correct_predicitons/len(predictions))


def prepare_images(label_names, labels_shuffled):
    prepared_dataset = []
    labels = []
    for label_name in label_names:
        prepared_dataset.extend(prepare_images_format(label_name, labels))

    pairs = unite_pairs(prepared_dataset, labels)

    shuffle(pairs)
    dataset = divide_pair(pairs, labels_shuffled)

    return dataset

def trim_endings(words):
    trimmed_words = []
    for word in words:
        word = word.replace(word[len(word)-5:len(word)], "")
        trimmed_words.append(word)
    return trimmed_words


train_labels = []
train_dataset = prepare_images(["shoes", "tshirt"], train_labels)
test_labels = []
test_dataset = prepare_images(["shoes_test", "tshirt_test"], test_labels)

mlp = MLPClassifier(hidden_layer_sizes=(64,32),
                    activation='logistic',
                    alpha=1e-4, solver='sgd',
                    tol=1e-4, random_state=1,
                    learning_rate_init=.1,
                    verbose=False)

mlp.fit(train_dataset, train_labels)

predictions = mlp.predict(test_dataset)

check_accuracy(predictions, test_labels)