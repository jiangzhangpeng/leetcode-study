# encoding:utf-8

from keras.layers import Dense, Dropout
from keras.models import Sequential

model = Sequential()
model.add(Dense(64, input_dim=784, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(10, activation='softmax'))

print(model.summary())
