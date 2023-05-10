import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing import image

model = keras.models.load_model('FCN/')

slika = tf.keras.utils.load_img('lv8\\test.png', color_mode="grayscale", target_size=(28, 28))

slika_arr = np.array(slika)
slika_arr = slika_arr.astype("float32")/255
slika_arr = np.expand_dims(slika_arr, -1)
slika_arr = np.reshape(slika_arr, (1, 28, 28, 1))



prediction = model.predict(slika_arr)

print(prediction)
prediction_class = np.argmax(prediction)
print("Predicted: ", prediction_class)