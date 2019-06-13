from flask import Flask, request, render_template
import contact_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/new_user')
def page():
    return render_template('user_form.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    d = contact_db.Database(endpoint, user, pass, db)
    processed_text = d.get_age(text.upper())
    return processed_text

@app.route('/new_user', methods=['POST'])
def create_account():
    name = request.form['name']
    age = request.form['age']
    d = contact_db.Database(endpoint, user, pass, db)
    processed_text = d.new_user(name.upper(), age.upper())
    return processed_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
