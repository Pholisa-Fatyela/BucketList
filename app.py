from flask import Flask, render_template    # Importing the flask module
app = Flask(__name__)

# Defininng a basic route and its corresponding request handler
@app.route("/")
def main():
    return render_template('index.html')

# Checking if executed file is the main program and run the app
if __name__ == "__main__":
    app.run()
