from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import user, show
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new')
def add_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    return render_template('new_show.html', user=user.User.get_by_user_id(data))

@app.route('/new/create', methods=['POST'])
def add_new_show():
    if 'user_id' not in session:
        return redirect('/')
    if not show.Show.validate_show(request.form):
        return redirect('/dashboard')
    data = {
        'title' : request.form.post['title'],
        'network' : request.form['network'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
        'user_id' : session['user_id'],
    }
    show.Show.save(data)
    return redirect('/dashboard')


@app.route('/edit/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('edit.html', user=user.User.get_by_user_id(user_data), show=show.Show.get_by_show_id(data))

@app.route('/update/post', methods=['POST'])
def update_post():
    if 'user_id' not in session:
        return redirect('/logout')
    if not show.Show.validate_show(request.form):
        return redirect(f'/edit/{request.form["id"]}')
    data = {
        'title' : request.form['title'],
        'network' : request.form['network'],
        'release_date' : request.form['release_date'],
        'description' : request.form['description'],
        'user_id' : session['user_id'],
    }
    show.Show.update(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data= {
        'id': id
    }
    user_data = {
        'id': session['user_id']
    }
    return render_template('show.html', user=user.User.get_by_user_id(user_data),shows=show.Show.get_all_shows(), show=show.Show.get_by_show_id(data))

@app.route('/delete/<int:id>')
def delete_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    show.Show.delete(data)
    return redirect('/dashboard')