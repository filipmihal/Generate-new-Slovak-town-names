from __future__ import absolute_import, division, print_function

import os

from six import moves

import ssl
import csv
import tflearn
from tflearn.data_utils import *

DATA_PATH = "../data/Slovak_towns.csv"
# Maximum length of generated names
MAXLEN = 20

OUTPUT_PATH = "output.csv"
OUTPUT_FILE = open(OUTPUT_PATH, "w+")
with open(DATA_PATH, newline='') as csvfile:
    source_towns = list(csv.reader(csvfile))

# Translate text file to vectors
X, Y, char_idx = textfile_to_semi_redundant_sequences(DATA_PATH, seq_maxlen=MAXLEN, redun_step=3)

# Create LSTM model
model = tflearn.input_data(shape=[None, MAXLEN, len(char_idx)])

model = tflearn.lstm(model, 512, return_seq=True)

model = tflearn.dropout(model, 0.5)

model = tflearn.lstm(model, 512)

model = tflearn.dropout(model, 0.5)

model = tflearn.fully_connected(model, len(char_idx), activation="softmax")

model = tflearn.regression(model, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.001)

# Generate city names
model = tflearn.SequenceGenerator(model,
                                  dictionary=char_idx,
                                  seq_maxlen=MAXLEN,
                                  clip_gradients=5.0,
                                  checkpoint_path="model_us_cities")

# training
for i in range(60):
    seed = random_sequence_from_textfile(DATA_PATH, MAXLEN)
    model.fit(X, Y, validation_set=0.2, batch_size=128, n_epoch=1)
    new_names = model.generate(30, temperature=1.2, seq_seed=seed).split('\n')
    for new_name in new_names:
        if new_name not in source_towns:
            OUTPUT_FILE.write(new_name + "\n")
