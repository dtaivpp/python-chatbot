
from transit.writer import Writer
from transit.reader import Reader
import websocket

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

try:
    import thread
except ImportError:
    import _thread as thread
import time

io = StringIO()
writer = Writer(StringIO(), "json") # or "json-verbose", "msgpack"
#writer.write(value)

reader = Reader("json") # or "msgpack"
#val = reader.read(io)

url = "ws://localhost:3449/chat?name=ChAI&room=Test"

def on_message(ws, message):
    print(reader.read(StringIO(message)))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")


def on_open(ws):
 #writer.write()
 #sender_data = io.getvalue()
  ws.send("[\"~:post-message\",\"YOYOYOYOYO\"]")
    #def run(*args):
        #for i in range(3):
         #   time.sleep(1)
        #time.sleep(1)
        #ws.close()
        #print("thread terminating...")
    #thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


