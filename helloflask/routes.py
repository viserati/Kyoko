from flask import render_template, url_for, flash, redirect
from helloflask import app
from helloflask.forms import RegistrationForm, LoginForm
from helloflask.models import User, Post

posts = [
    {
        'author': 'Emory Cole',
        'title': 'Intel Signal 0.001',
        'content': 'Detail content',
        'date_posted': 'April 04, 2020'
    },
    {
        'author': 'Anne Denton',
        'title': 'Intel Signal 0.002',
        'content': 'Detail content',
        'date_posted': 'April 14, 2020'
    },

    {
        'author': 'Melena Biento',
        'title': 'Intel Signal 0.003',
        'content': 'Detail content',
        'date_posted': 'April 18, 2020'
    }


]

@app.route("/") # This is a decorator or s fnction that wraps itself around another function.
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
