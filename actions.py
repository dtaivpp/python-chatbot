from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionBanner(Action):
  def name(self):
    return 'action_get_name'
  
  def run (self, dispatcher, tracker, domain):
    # Insert API call here
    bannerid = tracker.get_slot('bannerid')
    name = "David"  #Name returned by the API

    response = """Your name is {} and your ID is {}. """.format(name, bannerid)
    
    dispatcher.utter_message(response)
    return[SlotSet('system_name', name if name is not None else '')]

class ActionChatName(Action):
  def name(self):
    return 'action_chat_name'
  
  def run (self, dispatcher, tracker, domain):
    # Insert API call here
    #name = tracker.get_slot('chat_name')
    name = "Jeff"
    #Name returned by the API
    print(dispatcher)
    response = """Your chat name is {}""".format(name)

    dispatcher.utter_message(response)
    return[SlotSet('chat_name', name if name is not None else '')]