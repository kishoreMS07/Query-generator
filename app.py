import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample data
questions = ["What is your name?", "How are you?", "What do you do?"]
queries = ["My name is John.", "I'm fine, thank you.", "I'm a software engineer."]

# Tokenize and pad sequences
vocab_size = 1000  # Set your vocabulary size accordingly
max_len = 10  # Set your maximum sequence length accordingly

tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
tokenizer.fit_on_texts(questions + queries)

tokenized_questions = tokenizer.texts_to_sequences(questions)
tokenized_queries = tokenizer.texts_to_sequences(queries)

padded_questions = pad_sequences(tokenized_questions, maxlen=max_len, padding='post')
padded_queries = pad_sequences(tokenized_queries, maxlen=max_len, padding='post')

# Define the model
embedding_dim = 50  # Set your embedding dimension accordingly

model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_len),
    LSTM(64),
    Dense(vocab_size, activation='softmax')  # Adjust units based on your task
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
labels = np.arange(len(padded_queries))  # Example labels, adjust accordingly
model.fit(padded_questions, labels, epochs=10, batch_size=1)

