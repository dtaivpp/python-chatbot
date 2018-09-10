from rasa_core.channels import HttpInputChannel
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from load_bot import run_bot
import os

def run_slack_bot():
  print("Loading agent...")
  # load your trained agent
  agent = run_bot()

  print("Agent loaded.")

  input_channel = SlackInput(
    slack_token = os.environ['SLACK_TOKEN'],  # this is the `bot_user_o_auth_access_token`
  )

  print("Starting server on port 5004")
  agent.handle_channel(HttpInputChannel(5004,"/app", input_channel))

if __name__ == "__main__":
  run_slack_bot()
