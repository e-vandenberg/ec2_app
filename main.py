from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

app.run(host="0.0.0.0", port=80)
