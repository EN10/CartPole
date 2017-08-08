from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(2, input_shape=(4,), activation="softmax"))

model.compile(
	loss="categorical_crossentropy",
	optimizer="adam",
	metrics=["accuracy"])
