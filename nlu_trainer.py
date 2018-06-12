from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, nlu_config, directory):
  training_data = load_data(data)
  trainer = Trainer(config.load(nlu_config))
  trainer.train(training_data)
  model_directory = trainer.persist(directory, fixed_model_name = 'nlu')

if __name__ == '__main__':
  train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
