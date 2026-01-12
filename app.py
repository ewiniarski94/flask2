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

@app.route('/deleteMovies', methods=['POST'])
def delete_movies():
    
    ids = request.form.getlist('movieToRemove')
    if ids:
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        placeholders = ','.join('?' for _ in ids)
        query = f"DELETE FROM movies WHERE id IN ({placeholders})"
        cursor.execute(query, ids)
        db.commit()
        db.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
     app.run()