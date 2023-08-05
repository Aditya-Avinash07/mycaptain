import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample text data (replace this with your own dataset)
text_data = """
Alice was beginning to get very tired of sitting by her sister on the bank, 
and of having nothing to do. Once or twice she had peeped into the book her 
sister was reading, but it had no pictures or conversations in it, "and what 
is the use of a book," thought Alice, "without pictures or conversation?"
"""

# Tokenize the text data and create word sequences
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text_data])
total_words = len(tokenizer.word_index) + 1

sequences = []
for line in text_data.split('\n'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_sequence = token_list[:i+1]
        sequences.append(n_gram_sequence)

# Pad sequences to have the same length
max_sequence_length = max([len(seq) for seq in sequences])
sequences = pad_sequences(sequences, maxlen=max_sequence_length, padding='pre')

# Separate input and output sequences
X, y = sequences[:, :-1], sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)

# Build the LSTM model
model = Sequential([
    Embedding(total_words, 100, input_length=max_sequence_length-1),
    LSTM(150),
    Dense(total_words, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, verbose=1)

# Generate text using the trained model
seed_text = "Alice was"
generated_text = seed_text

for _ in range(20):
    token_list = tokenizer.texts_to_sequences([seed_text])[0]
    token_list = pad_sequences([token_list], maxlen=max_sequence_length-1, padding='pre')
    predicted_token_index = np.argmax(model.predict(token_list), axis=-1)
    predicted_word = tokenizer.index_word[predicted_token_index[0]]
    generated_text += " " + predicted_word
    seed_text += " " + predicted_word

print("Generated Text:")
print(generated_text)
