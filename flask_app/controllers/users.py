from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route('/users')
def home():
    users = User.get_all()
    return render_template("users.html", all_users=users)


@app.route('/users/new')
def add_form():
    return render_template("add-user.html")


@app.route('/add', methods=["POST"])
def add_one():
    if not User.validate_user(request.form):
        session['first_name'] = request.form.get('first_name')
        session['last_name'] = request.form.get('last_name')
        return redirect('/users/new')
    
    User.save(request.form)
    return redirect ('/users')


@app.route('/users/<int:user_id>')
def show_one(user_id):
    user = User.show_one(user_id)
    return render_template('show-one.html', user=user)

@app.route('/users/<int:user_id>/update')
def update(user_id):
    return render_template("update.html", user_id=user_id)


@app.route('/update_one', methods=["POST"])
def update_one():
    User.update_one(request.form)
    print(request.form['user_id'])

    return redirect("/users")

@app.route('/users/<int:user_id>/delete')
def delete(user_id):
    User.delete_one(user_id)
    return redirect('/users')