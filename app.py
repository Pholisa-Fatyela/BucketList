from flask import Flask, render_template, json, request    # Importing the flask module
app = Flask(__name__)

# Defininng a basic route and its corresponding request handler
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route("/signUp", methods=['POST'])
def signUp():
    # create user code will be here!!
    # read the posted values from th UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # validate the recieved values
    if _name and _email and _password:
        return json.dump({'html':'<span>All fields good !!</span>'})
    else:
        return json.dump({'html':'<span>Enter the required fields</span>'})


# Checking if executed file is the main program and run the app
if __name__ == "__main__":
    app.run()
