from flask import Flask
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index(): #view function
    user_agent = request.headers.get('User-Agent')
    return '<p> Your browser is %s</p>' %user_agent
    
if __name__ == '__main__':
    manager.run()
    