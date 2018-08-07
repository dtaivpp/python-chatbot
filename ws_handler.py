
from dialogue_management_model import run_student_bot
import websocket
import random
from transit.reader import Reader
from transit.writer import Writer

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# In Case we want to use multiple threads
try:
    import thread
except ImportError:
    import _thread as thread
import time

# Creates the writer 
io = StringIO()
writer = Writer(StringIO(), "json")

# Creates the reader
reader = Reader("json") 

# Gets the agent
agent = run_student_bot()

# Url For the Websocket
url = "ws://emscript.regent.edu:3449/chat?name=ChAI&room=ChatTest"


# Defines the action to do on reciept of a message
def on_message(ws, message):

  # Uses the transit reader to parse the recieved message
  data = reader.read(StringIO(message))

  # Checks to see if it is a new message
  if(data[0].str == 'new-messages'):
    # Creates variable for the user that sent the message
    user = list(data[1][0].values())[2]

    # Creates a variable for the message itself
    message = list(data[1][0].values())[3]

    # Ensures it does not respond to system messages or itself
    if(list(data[1][0].values())[2] != 'SYSTEM' and list(data[1][0].values())[2] != 'ChAI'):

      # Uses the agent defined earlier and the handle_message method to get the appropriate responce
      # Takes in:
      # - The message to interprete
      # - The senders name
      reply = agent.handle_message(text_message = message, sender_id= user)

      # Sleep for a moment because it makes it seem more realistic
      time.sleep(2)
      
      # Sends the response back to the user
      send_message(ws, reply[0]['text'])


# Simple error handling
def on_error(ws, error):
  print(error)


# Prints message on close
def on_close(ws):
  print("### closed ###")


# Defines how to send a message back 
def send_message(ws, message):
  ws.send("[\"~:post-message\",\"" + message + "\"]")


#
def on_open(ws):
  # Send an initial message to the users
  send_message(ws, "Hello world, I am ChAI!")


#
if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()



