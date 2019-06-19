from flask import Flask, request, render_template
import contact_db
import config

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/new_user')
def page():
    return render_template('user_form.html')

@app.route('/math')
def math():
    return render_template('calculate.html')

@app.route('/', methods=['POST'])
def form_post():
    text = request.form['text']
    d = contact_db.Database(config.endpoint, config.user, config.pwd, config.db)
    processed_text = d.get_age(text.upper())
    return processed_text

@app.route('/new_user', methods=['POST'])
def create_account():
    name = request.form['name']
    age = request.form['age']
    d = contact_db.Database(config.endpoint, config.user, config.pwd, config.db)
    processed_text = d.new_user(name.upper(), age.upper())
    return processed_text

@app.route('/math', methods=['POST'])
def calculate():
    x = request.form['num']
    processed_text = str((int(x.upper()) * 10) + 3)
    return processed_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
