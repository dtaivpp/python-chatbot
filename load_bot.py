# Used this to load the bot into a handler

import logging

from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

# Starts the bot for interacting with people
def run_bot(serve_forever=True):
  interpreter = RasaNLUInterpreter('./models/nlu/default/nlu')
  # Loads the previously trained dialogue model
  agent = Agent.load('./models/dialogue', interpreter = interpreter)

  if serve_forever:
    return agent


if __name__ == '__main__':
  run_bot()