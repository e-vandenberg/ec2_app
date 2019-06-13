from flask import Flask, request, render_template
import contact_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    d = contact_db.Database(endpoint, user, pass, db)
    processed_text = d.get_age(text.upper())
    return processed_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
