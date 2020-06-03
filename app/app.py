from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
dbconn = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = dbconn.nycares_db
# Get source data for dynamically populated templates
# source_df = pd.read_csv('indeed_cleaned.csv')

# jobs = []
# jobs = db.jobs.find().limit(300)
# # Set index / set counter to 1
# i = 1

# Define routes
@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/results.html")
def Visualization():
    return render_template('results.html')


# @app.route("/il-data.html")
# def ViewILData():
#     jobs = db.jobs.find().limit(50)
#     return render_template('il-data.html', jobs=jobs)


# @app.route("/team.html")
# def About():
#     return render_template('team.html')


if __name__ == '__main__':
    app.run(debug=True)
