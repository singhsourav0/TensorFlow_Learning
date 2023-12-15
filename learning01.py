#TensorFlow learning journy.....

# Simple exaple of machine learning code that recognize activity of person.
if (speed< 4) {
  status = walking;
}

else if(speed < 12){
  status = Running;
}
else {
  status = Bikig
}


# Simple machine Learning code as  Helo world in tensorflow.
import tensorflow as tf
import numpy as np
from tensorflow import keras

print(tf.__version__)

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))
