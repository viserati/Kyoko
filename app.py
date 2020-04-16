from flask import Flask, render_template, url_for
app = Flask(__name__)

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


# Code below is so you don't have to turn the server on/off after each change.
if __name__ == '__main__':
	app.run(debug=True)
