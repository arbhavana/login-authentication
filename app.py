from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure value

# Sample user data (you should replace this with a database)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

# Function to check if a user is logged in
def is_logged_in():
    return 'username' in session

# Route for the login page
@app.route('/')
def login():
    if is_logged_in():
        return redirect('/secured')
    return render_template('login.html')

# Route to handle the login form submission
@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        session['username'] = username
        return redirect('/secured')
    
    return 'Invalid login credentials. <a href="/">Try again</a>'

# Route for the secured page
@app.route('/secured')
def secured():
    if is_logged_in():
        return render_template('secured.html')
    return redirect('/')

# Route to logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
