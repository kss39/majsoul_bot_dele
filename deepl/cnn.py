import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from glob import glob

list_img = glob('resources/train_set/*.png')

ds_train = keras.preprocessing.image_dataset_from_directory(
    'resources/train_set/',
    labels='inferred',
    batch_size=128,
    image_size=(66, 105)
)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(66, 105, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dropout(0.05))
model.add(layers.Dense(38))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(ds_train, epochs=200, batch_size=128)
model.save('deepl/tile_model')
