from rasa_core.channels import HttpInputChannel
from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
from load_bot import run_bot
import json

def run_slack_bot():
  # load your trained agent
  agent = run_bot()
  filename = "slack_creds.json"

  #Read JSON data into the datastore variable
  if filename:
    with open(filename, 'r') as f:
        credentials = json.load(f)

  input_channel = SlackInput(
    slack_token= credentials['token'],  # this is the `bot_user_o_auth_access_token`
    slack_channel ="augustine"  # the name of your channel to which the bot posts (optional)
  )

  agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))

if __name__ == "__main__":
  run_slack_bot()