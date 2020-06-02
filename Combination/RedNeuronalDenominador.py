import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

def main():
    df = pd.read_csv('Interpolation/InterpolatedDenMonth.csv')
    dataset = df.values
    X = dataset[:,1:7]
    Y = dataset[:,7]
    min_max_scaler = preprocessing.MinMaxScaler()
    X_scale = min_max_scaler.fit_transform(X)
    X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.2)
    X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
    model = Sequential([
    Dense(6, activation='softplus', input_shape=(6,)),
    Dense(32, activation='softplus'),
    Dense(12, activation='softplus'),
    Dense(1, activation='softplus'),
    ])
    model.compile(optimizer='rmsprop',
              loss='mean_absolute_error')
    hist = model.fit(X_train, Y_train,
          batch_size=128, epochs=1500,
          validation_data=(X_val, Y_val))
        # serialize model to JSON
    model_json = model.to_json()
    with open("modelden.json", "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights("modelden.h5")
    print("Saved model to disk")

if __name__ == "__main__":
    main()