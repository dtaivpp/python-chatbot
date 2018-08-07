from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

# This is used to train the rasa nlu
def train_nlu(data, nlu_config, directory):
  # Loads the intent training data
  training_data = load_data(data)

  # Creates an instance of the Trainer using the nlu_config
  trainer = Trainer(config.load(nlu_config))

  # Starts the training
  trainer.train(training_data)

  # Saves the trained model in the specified directory with the specified name
  trainer.persist(directory, fixed_model_name = 'nlu')

if __name__ == '__main__':
  # Calls the trainer function
  # Takes in:
  # - Training data file
  # - Spacy trainer config file
  # - Output directory
  train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')