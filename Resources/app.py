# import dependencies 
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd 


engine = create_engine("sqlite:///db2.sqlite")

print(pd.read_sql("SELECT * FROM infant", engine))

Base = automap_base()

Base.prepare(engine, reflect=True)

infant_ = Base.classes.infant

# create an app, pass __name__
app = Flask(__name__)

# Define what to do when users hits the index route
@app.route("/")
def home():
    return (
        f"Available Routes:<br>"
        f"/api/v1.0/infants"
    )

@app.route("/api/v1.0/infants")
def infants():
    session = Session(engine)

    results = session.query(infant_.YEAR, infant_.STATE, infant_.RATE, infant_.DEATHS).all()

    session.close()

    all_info = []
    for YEAR, STATE, RATE, DEATHS in results:
        data_dict = {}
        data_dict["Year"] = YEAR,
        data_dict["State"] = STATE,
        data_dict["Rate per 1000"] = RATE,
        data_dict["Deaths"] = DEATHS
        all_info.append(data_dict)
        
    
    return jsonify(all_info)

if __name__ == "__main__":
    app.run(debug=True)
