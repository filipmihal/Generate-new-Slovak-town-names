# Generate new Slovak town names
## About
Generating new town names using a LSTM network on Tensorflow TFLearn and a dataset of all town names of Slovakia.
More info about LSTM: [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) <br/>
Selection of the best names that were generated is located in [output.txt](output.txt)

## Prerequisites
Python 3.5

You can find all required python packages in [requirements.txt](requirements.txt)<br/>
`pip install -r requirements.txt` 

## Run
`python data/get_town_list.py` <br/>
get all Slovak town names from this website and parse them to csv format.

`python model/name_generator.py` <br/>
generate new town names and save them to model/output.csv