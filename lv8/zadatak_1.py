import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay



# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.figure("Prva slika")
plt.imshow(x_train[0], cmap='gray')
plt.figure("Druga slika")
plt.imshow(x_train[2], cmap='hot')
plt.figure("Treca slika")
plt.imshow(x_train[4], cmap='gray')
plt.show()
# ispis oznake u terminal
print("Oznaka: ", y_train[2])


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = keras.Sequential(
    [
        layers.Flatten(input_shape=(28, 28, 1)),
        layers.Dense(100, activation="relu"),
        layers.Dense(50, activation="relu"),
        layers.Dense(10, activation="softmax"),
    ]
)

print(model.summary())



# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)



# TODO: provedi ucenje mreze

batch_size=32
epochs=20
history = model.fit(x_train_s,y_train_s,batch_size=batch_size,epochs=epochs,validation_split=0.1)
predictions = model.predict(x_test_s)
score = model.evaluate(x_test_s,y_test_s,verbose=0)

predictions=np.argmax(predictions, axis=1) 
y_test_s=np.argmax(y_test_s, axis=1) 


# TODO: Prikazi test accuracy i matricu zabune

cm=confusion_matrix(y_test_s, predictions)

cm_display=ConfusionMatrixDisplay(cm)
cm_display.plot()
plt.show()

# TODO: spremi model

model.save("FCN/")
del model