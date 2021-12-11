import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from PIL import Image

data_path = os.path.join("","C:\\Users\\kirut\\Documents\\smile_rec\\data")

image_size = 224
batch_size = 64

data_gen = keras.preprocessing.image.ImageDataGenerator(vertical_flip=False,rescale=1/255,validation_split=0.1)

data = data_gen.flow_from_directory(data_path,target_size=(image_size, image_size),
                batch_size=batch_size,
                class_mode='binary',
                seed = 52,
                subset="training")

val = data_gen.flow_from_directory(data_path,target_size=(image_size, image_size),
                batch_size=batch_size,
                class_mode='binary',
                seed = 52,
                subset="validation")

IMG_SHAPE = (image_size, image_size,3)

base_model = tf.keras.applications.NASNetMobile(include_top=False,input_shape=IMG_SHAPE,weights="imagenet",pooling="avg")

base_model.trainable = False

model = tf.keras.Sequential([
    base_model,
    keras.layers.Dense(100,activation="elu"),
    keras.layers.Dense(1,activation='sigmoid')
])

optimizer = keras.optimizers.Nadam(lr=1e-3)

loss = keras.losses.binary_crossentropy

model.compile(optimizer=optimizer,loss=loss,metrics=["acc"])
epochs = 50
lr = tf.keras.callbacks.ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.1,
    patience=2)
es = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=epochs//5, verbose=1, mode='auto', baseline=None, restore_best_weights=True)
steps_per_epoch = data.n//batch_size
val_steps_per_epoch = val.n//batch_size+1
model.fit(data,epochs=epochs,validation_data=val,steps_per_epoch=steps_per_epoch,validation_steps = val_steps_per_epoch,callbacks=[lr,es])

model.save("final.h5")
