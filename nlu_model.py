from rasa_nlu.model import Metadata, Interpreter

# Quick test to run the model
def run_nlu ():
  interpreter = Interpreter.load('./models/nlu/default/nlu')
  print(interpreter.parse(u"Id B04010203"))

if __name__ == '__main__':
  run_nlu()
