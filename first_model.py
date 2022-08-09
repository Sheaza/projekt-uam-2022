def initialize_network():
    model = Sequential()
    model.add(Conv2D(filters=10, kernel_size=1, activation='relu', input_shape=(8,8,12)))
    model.add(MaxPooling2D(pool_size=2, strides=None))
    model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=None))
    model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=2, strides=None))
    model.add(Conv2D(filters=10, kernel_size=1, activation='relu'))
    model.add(Flatten())
    model.add(BatchNormalization())
    model.add(Dense(1,activation = 'sigmoid'))
    return model