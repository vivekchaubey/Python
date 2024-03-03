import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Define the input sequence as a nested list
nested_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [221, 222, 223, 224, 225]
]

# Prepare the data for training
X = np.array(nested_list[:-1])  # Input sequences
y = np.array(nested_list[1:])   # Output sequences (next list item)

# Reshape the data for LSTM input
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Define the LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(5))  # Output layer with 5 units (length of each list item)
model.compile(loss='mse', optimizer='adam')

# Train the model
model.fit(X, y, epochs=10000, verbose=0)

# Generate the next list item in the sequence
next_input = np.array([nested_list[-1]])  # Use the last item in the input sequence
next_input = next_input.reshape((1, 1, next_input.shape[1]))
prediction = model.predict(next_input)
print(next_input)

print("Predicted next list item:")
print(prediction)
