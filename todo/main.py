from flask import Flask, render_template

app = Flask(__name__)

class Todo():
  def __init__(self, title, done):
    self.title = title
    self.done = done

todos = [Todo("one", False), Todo("two", True)]

@app.route("/")
def index():
  """
  This method renders a template which displays all the Todos.
  If there are no Todos it simply says "Nothing to do!"
  """
  return render_template('index.html', todos=todos, ntodos=len(todos))

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True, port=5000)
