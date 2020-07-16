from tensorflow import keras
import tensorflowjs as tfjs

model = keras.models.load_model("final.h5")
model.save("final")
tfjs.converters.tf_saved_model_conversion_v2.convert_tf_saved_model("final","tfjs.json")
