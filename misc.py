<!DOCTYPE html>
<html>
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename= 'main.css')}}">


      {% if title %}
        <title>Flask Blog - {{ title }}</title>
      {% else %}
        <title>Flask Blog</title>
      {% endif %}

  </head>
  <body>

    <header class="site-header">
      <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
        <div class="container">
          <a class="navbar-brand mr-4" href="/">Flask Blog</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarToggle">
            <div class="navbar-nav mr-auto">
              <a class="nav-item nav-link" href="/">Home</a>
              <a class="nav-item nav-link" href="/about">About</a>
            </div>
            <!-- Navbar Right Side -->
            <div class="navbar-nav">
              <a class="nav-item nav-link" href="/login">Login</a>
              <a class="nav-item nav-link" href="/register">Register</a>
            </div>
          </div>
        </div>
      </nav>
    </header>

    <main role="main" class="container">
  <div class="row">
    <div class="col-md-8">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {%  if messages %}
                {% for category, message in messages %}

                    <div class="alert alert-{{category}}">
                        {{ message }}
                    </div>

                {% endfor %}
            {%  endif %}
        {% endwith %}
      {% block content %}{% endblock %}
    </div>
    <div class="col-md-4">
      <div class="content-section">
        <h3>Our Sidebar</h3>
        <p class='text-muted'>You can put any information here you'd like.
          <ul class="list-group">
            <li class="list-group-item list-group-item-light">Latest Posts</li>
            <li class="list-group-item list-group-item-light">Announcements</li>
            <li class="list-group-item list-group-item-light">Calendars</li>
            <li class="list-group-item list-group-item-light">etc</li>
          </ul>
        </p>
      </div>
    </div>
  </div>
</main>



    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>

-----------------------------------------
------Register-----

{% extends "layout.html" %}
{% block content %}

  <div class="content-section">
      <form method="post" action="">
          {{ form.hidden_tag() }}
          <fieldset class="form-group">
              <legend class-"border-bottom mb-4">Join Today</legend>

              <div class="form-group">
                {{ form.username.label(class="form-control-label") }}
                {{ form.username(class="form-control form-control-lg") }}
              </div>

              <div class="form-group">
                {{ form.email.label(class="form-control-label") }}
                {{ form.email(class="form-control form-control-lg") }}
              </div>

              <div class="form-group">
                {{ form.password.label(class="form-control-label") }}
                {{ form.password(class="form-control form-control-lg") }}
              </div>

              <div class="form-group">
                {{ form.confirm_password.label(class="form-control-label") }}
                {{ form.confirm_password(class="form-control form-control-lg") }}
              </div>

          </fieldset>

          <div class="form-group">
            {{ form.submit(class="btn btn-outline-info") }}
          </div>


      </form>

  </div>
  <div class="border-top pt-3">
      <small class="text-muted">
          Already have an account? <a class=ml-2 href= "{{ url_for('login') }}"> Sign In</a>

  </div>

{% endblock content %}

-------------------------

app.py---------copyright

from flask import Flask, render_template, url_for, flash, redirect
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for, {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title = 'Login', form = form)

# Code below is so you don't have to turn the server on/off after each change.
if __name__ == '__main__':
	app.run(debug=True)
