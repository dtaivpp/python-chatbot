from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import (MaxHistoryTrackerFeaturizer,
                                   BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

# This is used to train the RASA core on your dialogue model
# and branching statements. It is a CLI trainer
def run_student_online(input_channel, interpreter,
                          domain_file="student_info_domain.yml",
                          training_data_file='data/stories.md'):

  # Featureizer Generation
  featurizer = MaxHistoryTrackerFeaturizer(BinarySingleStateFeaturizer(), max_history=5)
  
  # Not really sure what is happening here
  agent = Agent(domain_file,
                policies=[MemoizationPolicy(max_history=5),
                          KerasPolicy(featurizer)],
                          interpreter=interpreter)

  # This is where our training data file is loaded in for training
  training_data = agent.load_data(training_data_file)
  
  # Training data is the training data object created in the above line
  # 
  # Epochs are the number of runs the bot does
  agent.train_online(training_data,
                      input_channel=input_channel,
                      batch_size=50,
                      epochs=400,
                      max_training_samples=300)

  return agent


if __name__ == '__main__':
  logging.basicConfig(level="INFO")
  nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/nlu')
  run_student_online(ConsoleInputChannel(), nlu_interpreter)