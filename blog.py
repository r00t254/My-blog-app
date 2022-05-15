from flask import Flask,render_template,flash,redirect,url_for
from datetime import datetime
from flask_sqlaichemy import SQLAIchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import date
from webforms import loginForm,PostForm,UserForm,PasswordForm,NameForm,SearchForm
from flask_login import UserMixin,Login_user,LoginManager,login_required,logout_user
from webforms import loginForm,PostForm,UserForm,PasswordForm,NameForm


# create a Flask Instance
app = Flask(__name__)
# Add Database
# Old SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite'
# New MySQL DB
# app,config[SQLALCHEMY_DATABASE_URI] = 'mysqlalchemy'

# Secreate Key
app.config['SECRETE_KEY'] ='my super secret key'
db =SQLAIchemy(app)
migrate = Migrate(app,db)
# flask_login stuff
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_use(user_id):
    return Users.query.get(int(user_id))

# Create Search Function
@app.route('/search',ethods=["POST"])
def search():
        form = SearchForm()
        if form.validate_on_submit():
            post.searched = form.searched.data
            return render_template("search.html",form=form,searched =post.searched)

# Create Login Page
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form)
        if user:
            # check the hash
            if check_password_hash(user.check_password_hash):
                Login_user(user)
                flash("login Successful")
                return redirect(url_for('dashboard'))
            else:
                flash("Wrong Password -Try Again")

