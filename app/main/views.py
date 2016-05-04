from datetime import datetime
from flask import render_template,session,redirect,url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

# @main.route('/',methods=['GET','POST'])
# def index():
#     form = NameForm()
#     if form.validate_on_submit():
#         pass
#         return redirect(url_for('.index'))
#     return render_template('index.html',form=from,name=session.get('name'),
#         known=session.get('known',False),
#         current_time=datetime.utcnow())

#路由修饰器由蓝本提供，url_for()函数的第一个参数是路由的端点名
@main.route('/')
def index():
    return render_template('index.html')