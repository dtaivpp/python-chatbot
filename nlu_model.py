from rasa_nlu.model import Metadata, Interpreter

# Quick test to run the model
def run_nlu ():
  # Rasa NLU interpereter to read the model
  interpreter = Interpreter.load('./models/nlu/default/nlu')
  
  #Print the results of the test case
  print(interpreter.parse(u"Id B04010203"))

if __name__ == '__main__':
  run_nlu()
