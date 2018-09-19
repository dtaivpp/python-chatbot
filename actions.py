from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.actions.forms import FormAction
from rasa_core.actions.Action import EntityFormField
from rasa_core.events import SlotSet
# from requests_ntlm import HttpNtlmAuth
import requests
import json
import re

# These are custom actions for the Chatbot
# It accepts an action from RASA.Core
class ActionBanner(Action):
  def name(self):
    # Here is where the name of the action is returned
    # to student_info_domain.yml for use in 
    # dialogue trainer
    return 'action_get_name'
  
  def run (self, dispatcher, tracker, domain):
    # Pulls name from the banner ID slot created in
    # student_info_domain.yml
    bannerid = tracker.get_slot('bannerid')
    
    # Example of how an api call can be used to get a name
    name = Get_Name(bannerid)

    # This is the response that is sent back to the 
    # user with this action
    response = """Your name is {}""".format(name)
    
    # This tells the agent to send the user back the response
    dispatcher.utter_message(response)

    # Here we are telling the system that the data we just
    # got from the api should fill the system_name
    return[SlotSet('system_name', name if name is not None else '')]

class ActionChatName(Action):
  def name(self):
    return 'action_chat_name'
  
  def run (self, dispatcher, tracker, domain):
    # When you call the Agent with a sender ID you can
    # access that here with the dispatcher object
    if not dispatcher['sender_id']:
      name = "Steve" 
    else:
      name = dispatcher['sender_id']
    
    # Creates the response message
    response = """Your chat name is {}""".format(name)

    # This tells the agent to send the user back the response
    dispatcher.utter_message(response)

    # Here we are telling the system that the data we just
    # got from sender id should fill the chat_name slot
    return[SlotSet('chat_name', name if name is not None else '')]

def Get_Name(erpid):
  # API Stump
  # You can create custom api functions like here to 
  # get data for the users
  return "Jeff" 


class ActionFillApp(FormAction):

    RANDOMIZE = True

    @staticmethod
    def required_fields():
        return [
            EntityFormField("f_name", "f_name"),
            EntityFormField("l_name", "l_name"),
            EntityFormField("phone_number", "phone_number")
        ]

    def name(self):
        return 'action_search_restaurants'

    def submit(self, dispatcher, tracker, domain):
        results = ""
        #results = RestaurantAPI().search(
        #    tracker.get_slot("cuisine"),
        #    tracker.get_slot("people"),
        #    tracker.get_slot("vegetarian"))
        return [SlotSet("search_results", results)]


class ActionRegexCheck(Action):

  def name(self):
    return 'action_regex_check'
  
  def run (self, dispatcher, tracker, domain):
    pattern = re.compile(r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")

    text_to_check = ""
    text_to_check = tracker.get_slot('input')

    if(pattern.match(text_to_check)):
      dispatcher.utter_message("It matched!")
      return [SlotSet('input', text_to_check if text_to_check is not None else '')]

    dispatcher.utter_message("That is not a valid input.")
    return[SlotSet('input', '')] 
