from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/index.html')
def home2():
    return home()

@app.route('/<file_name>')
def page_loader(file_name):
    return render_template(f'./{file_name}')

@app.route('/submit_form', methods = ['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        persist_contact(data)
        return redirect('thankyou.html')
    else:
        return 'try again'


def persist_contact(data):
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    with open('database.txt', 'a') as file:
        file.write(f'{email}|{subject}|{message}\n')
