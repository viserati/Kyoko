from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '137affc4bc7a432606e0532aa2e85310'

posts = [
    {
        'author' : 'Anthony Soprano',
        'title' : 'Posting 1',
        'content' : 'First post content ...',
        'date_posted' : 'April 15, 2020',
    },

    {
        'author' : 'Junior Soprano',
        'title' : 'Posting 2',
        'content' : 'Second post content ...',
        'date_posted' : 'April 16, 2020',

    }
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts = posts)

@app.route('/about')
def about():
	return render_template('about.html', title = 'About !!!')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

# Code below is so you don't have to turn the server on/off after each change.
if __name__ == '__main__':
	app.run(debug=True)
