from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def home():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = mars_scrape.scrape_all()
    mars.update({}, mars_data, upsert=True)
    return redirect('mongodb://localhost:27017')

if __name__ == "__main__":
    app.run(debug=True)

