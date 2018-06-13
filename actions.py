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
    return[SlotSet('name', name if name is not None else '')]
