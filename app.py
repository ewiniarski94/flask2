from flask import Flask, render_template, request, url_for, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    return render_template('home.html', movies=cursor)


@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear = request.form.get('year')
        movieActors = request.form.get('actors')

        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        query = f"INSERT INTO movies (title, year, actors) VALUES ('{movieTitle}','{movieYear}','{movieActors}')"
        cursor.execute(query)
        db.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
