from flask_admin import Admin,BaseView, expose
from flask import render_template
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash

from soccerlevel11.ext.database import db
from soccerlevel11.models import Video, User

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        arg1 = 'Hello'
        return self.render('admin/dashboard.html', arg1=arg1)

class UserAdmin(sqla.ModelView):
    column_list = ['username']
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.password = generate_password_hash(model.password)


admin = Admin(index_view=MyHomeView(name='DashBoard'))

def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.add_view(sqla.ModelView(Video, db.session))
    admin.add_view(UserAdmin(User, db.session, name='Users'))
    admin.init_app(app)