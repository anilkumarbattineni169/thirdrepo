# loginpage.py
from flask import Flask, render_template, request

app = Flask(__name__)

# Simple login check (change username/password as you want)
correct_username = "admin"
correct_password = "12345"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == correct_username and password == correct_password:
            return f"<h1 style='color:white;background:#007bff;text-align:center;padding:100px;'>Welcome {username}! Login Successful 😊</h1>"
        else:
            return render_template('loginpage.html', error="Wrong username or password!")

    return render_template('loginpage.html')

if __name__ == '__main__':
    app.run(debug=True)