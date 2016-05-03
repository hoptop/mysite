from flask import Flask,render_template
from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index(): #view function
    # user_agent = request.headers.get('User-Agent')
    return render_template('index.html')
    
if __name__ == '__main__':
    app.debug = True
    manager.run()
    