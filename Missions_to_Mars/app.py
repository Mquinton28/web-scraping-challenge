# Import Necessary Libraries
from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Create Route 
@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)