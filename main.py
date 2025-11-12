from flask import Flask
from flask import render_template
from flask import request
import database_manager as dbHandler

DEBUG = True

def debug(msg, *debug_content):
  if DEBUG:
    if msg:
        print("\n" + "=" * 100)
        print(msg + " :[DEBUG]")

        if any(debug_content):
          for content in debug_content:
              for item in content:
                if item:
                  print(" ")
                  print(item)

                else:
                  print(" ")
                  print(content)

        print("\n" + "=" * 100)

    else:
       
       print("\nNo content title.")

app = Flask(__name__)

@app.route('/index.html', methods=['GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
   data = dbHandler.listExtension()
   debug("DB data", data)
   return render_template('/index.html', content=data)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
