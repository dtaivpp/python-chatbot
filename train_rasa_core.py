from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)
from datetime import datetime

if __name__ == '__main__':
  start = datetime.now()
  logging.basicConfig(level='INFO')

  #File for dialog management
  training_data_file = './data/stories.md'
	#Save file for generated model
  model_path = './models/dialogue'

  #Featureizer Generation
  featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)

  # Domain and Policies needed
  agent = Agent('./data/student_info_domain.yml', policies=[MemoizationPolicy(max_history=5),
                                                     KerasPolicy(featurizer)])
	
  training_data = agent.load_data(training_data_file)

    
  # Training data is the training data object created in the above line
  # input_channel - How the trainer recieves its input
  # epochs - Number of training passes
  # batch_size - How many times the model is updated per pass
  # validation_split - Fraction of the training data to be used as validation data 
  # augmentation_factor - How many of the dialogue stories are randomly glued together
      # the more stories you have the higher the augmentation factor you want
  agent.train(
    training_data,
    batch_size=35,
    epochs=400,
    max_training_samples=200,
    validation_split = 0.2,
    augmentation_factor = 20)
	
  # Logging for time spent training
  end = datetime.now()
  final = end - start
  print("Time to train: " + str(final))
  
  # Save Model
  agent.persist(model_path)