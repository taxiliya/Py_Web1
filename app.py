from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import config
import datetime
app=Flask(__name__)
app.config.from_object(config.DbConfig)
db=SQLAlchemy(app)

class Song(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    song_name=db.Column(db.String(100),nullable=False)
    singer_name=db.Column(db.String(100),nullable=False)
    storage_time=db.Column(db.DateTime,default=datetime.datetime.now())

    def __init__(self,songname,singername):
        self.song_name=songname
        self.singer_name=singername

db.create_all()

@app.route('/Movie')
def index():
    songs=Song.query.all()
    return render_template('index.html',songset=songs)

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method=='POST':
        songname=request.form['songname']
        singername=request.form['singername']
        print(songname,singername)
        song1=Song(songname=songname,singername=singername)
        db.session.add(song1)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('add.html')

@app.route('/find',methods=['GET','POST'])
def find():
    if request.method == 'POST':
        songname = request.form['songname']
        songs = Song.query.filter_by(song_name=songname).all()
        if songs==[]:
            return redirect('/')
        else:
            return render_template('index.html',songset=songs)
    else:
        return redirect('/')

@app.route('/del_row',methods=['GET','POST'])
def del_row():
    if request.method == 'POST':
        songid = int(request.form['songid'])
        song = Song.query.get_or_404(songid)
        if song!=[]:
            db.session.delete(song)
            db.session.commit()
    return redirect('/')

@app.route('/go_edit_row',methods=['GET','POST'])
def go_edit_row():
    if request.method == 'POST':
        songid = int(request.form['songid'])
        song = Song.query.get_or_404(songid)
        if song == []:
            return redirect('/')
        return render_template('edit.html',song=song)
    else:
        return redirect('/')

@app.route('/edit_row',methods=['GET','POST'])
def edit_row():
    if request.method == 'POST':
        songid = request.form['songid']
        song = Song.query.filter_by(id=songid).first()
        song.song_name = request.form['songname']
        song.singer_name = request.form['singername']
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')

if __name__=='__main__':
    app.run(debug=True)