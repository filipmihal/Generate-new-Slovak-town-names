# Generate new Slovak town names
## About
Generating new town names using a LSTM network on Tensorflow TFLearn and a dataset of all town names of Slovakia.
More info about LSTM: [here](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) <br/>
Selection of the best names that were generated is located in [output.txt](output.txt) <br/>
My personal favorites: Parohovce, Semeňov, Bohovce, Nižná Kanov

One can use many datasets, for instance: [US first names](https://data.world/len/us-first-names-database) , [US city names](https://data.mongabay.com/igapo/US.htm)
## Prerequisites
Python 3.5

You can find all required python packages in [requirements.txt](requirements.txt)<br/>
`pip install -r requirements.txt` 

## Run
`python data/get_town_list.py` <br/>
get all Slovak town names from [this website](http://www.e-obce.sk/zoznam_vsetkych_obci.html) and parse them to csv format.

`python model/name_generator.py` <br/>
generate new town names and save them to model/output.csv

