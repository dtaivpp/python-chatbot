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
  agent = Agent('student_info_domain.yml', policies=[MemoizationPolicy(max_history=5),
                                                     KerasPolicy(featurizer)])
	
  training_data = agent.load_data(training_data_file)

  # Augmentation Factor - Fake stories created
  # Epochs - number of forwards and backwards training passes
  # Batch Size - How many entries it should use in each pass
  # Validation Split
  agent.train(
    training_data,
    augmentation_factor = 50,
    epochs = 500,
    batch_size = 10,
    validation_split = 0.2)
  end = datetime.now()
  final = end - start
  print(final)
  # Save Model
  agent.persist(model_path)