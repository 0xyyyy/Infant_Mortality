# import dependencies 
from flask import Flask, jsonify, render_template
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

birthweight = Base.classes.birthweight

unmarried = Base.classes.unmarried

teen = Base.classes.teen

medianincome = Base.classes.medianincome

infant_2018 = Base.classes.infantlatest

lowbirth2018 = Base.classes.birthweight2018

teen_2018 = Base.classes.teen2018

unmarried_2018 = Base.classes.unmarried2018

# create an app, pass __name__
app = Flask(__name__)

# Define what to do when users hits the index route
@app.route("/")
def home():
    return render_template('index.html')
        # f"Available Routes:<br>"
        # f"/api/v1.0/infants<br>"
        # f"/api/v1.0/birthweight<br>"
        # f"/api/v1.0/teen<br>"
        # f"/api/v1.0/unmarried<br>"
        # f"/api/v1.0/medianincome<br>"
@app.route("/view2.html")
def view2():
    return render_template('view2.html')

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
        data_dict["Rate_per_1000"] = RATE,
        data_dict["Deaths"] = DEATHS
        all_info.append(data_dict)
    return jsonify(all_info)       

@app.route("/api/v1.0/infants2018")
def infant2018():
    session = Session(engine)

    results = session.query(infant_2018.YEAR, infant_2018.STATE, infant_2018.RATE, infant_2018.DEATHS).all()

    session.close()

    all_info = []
    for YEAR, STATE, RATE, DEATHS in results:
        data_dict = {}
        data_dict["Year"] = YEAR,
        data_dict["State"] = STATE,
        data_dict["Rate_per_1000"] = RATE,
        data_dict["Deaths"] = DEATHS
        all_info.append(data_dict)
    return jsonify(all_info)

        
    

@app.route("/api/v1.0/birthweight")
def birthweights():
    session = Session(engine)

    results = session.query(birthweight.YEAR, birthweight.STATE, birthweight.RATE).all()

    session.close()

    bw_info = []
    for YEAR, STATE, RATE in results:
        bw_dict = {}
        bw_dict["Year"] = YEAR,
        bw_dict["State"] = STATE,
        bw_dict["Rate"] = RATE
        bw_info.append(bw_dict)

    return jsonify(bw_info)

@app.route("/api/v1.0/birthweight2018")
def birthweight2018():
    session = Session(engine)

    results = session.query(lowbirth2018.YEAR, lowbirth2018.STATE, lowbirth2018.RATE).all()

    session.close()

    all_lowbirth2018_info = []
    for YEAR, STATE, RATE in results:
        lowbirth_dict = {}
        lowbirth_dict["Year"] = YEAR,
        lowbirth_dict["State"] = STATE,
        lowbirth_dict["Rate"] = RATE
        all_lowbirth2018_info.append(lowbirth_dict)
    
    return jsonify(all_lowbirth2018_info)

@app.route("/api/v1.0/teen")
def teens():
    session = Session(engine)

    results = session.query(teen.YEAR, teen.STATE, teen.RATE).all()

    session.close()

    teen_info = []
    for YEAR, STATE, RATE in results:
        teen_dict = {}
        teen_dict["Year"] = YEAR,
        teen_dict["State"] = STATE,
        teen_dict["Rate"] = RATE
        teen_info.append(teen_dict)

    return jsonify(teen_info)

@app.route("/api/v1.0/teen2018")
def teen2018():
    session = Session(engine)

    results = session.query(teen_2018.YEAR, teen_2018.STATE, teen_2018.RATE).all()

    session.close()

    teen2018_info = []
    for YEAR, STATE, RATE, in results:
        teen2018_dict = {}
        teen2018_dict["Year"] = YEAR,
        teen2018_dict["State"] = STATE,
        teen2018_dict["Rate"] = RATE
        teen2018_info.append(teen2018_dict)
    
    return jsonify(teen2018_info)

@app.route("/api/v1.0/unmarried")
def unmarrieds():
    session = Session(engine)

    results = session.query(unmarried.YEAR, unmarried.STATE, unmarried.RATE).all()

    session.close()

    unmarried_info = []
    for YEAR, STATE, RATE in results:
        unmarried_dict = {}
        unmarried_dict["Year"] = YEAR, 
        unmarried_dict["State"] = STATE,
        unmarried_dict["Rate"] = RATE
        unmarried_info.append(unmarried_dict)
    
    return jsonify(unmarried_info)

@app.route("/api/v1.0/unmarried2018")
def unmarried2018():
    session = Session(engine)

    results = session.query(unmarried_2018.YEAR, unmarried_2018.STATE, unmarried_2018.RATE).all()

    session.close()

    unmarried2018_info = []
    for YEAR, STATE, RATE in results:
        unmarried2018_dict = {}
        unmarried2018_dict["Year"] = YEAR,
        unmarried2018_dict["State"] = STATE,
        unmarried2018_dict["Rate"] = RATE
        unmarried2018_info.append(unmarried2018_dict)
    
    return jsonify(unmarried2018_info)


@app.route("/api/v1.0/medianincome")
def medianincome_():
    session = Session(engine)

    results = session.query(medianincome.YEAR, medianincome.STATE, medianincome.MEDIANINCOME)

    session.close()

    medianincome_info = []
    for YEAR, STATE, MEDIANINCOME in results:
        medianincome_dict = {}
        medianincome_dict["Year"] = YEAR,
        medianincome_dict["State"] = STATE,
        medianincome_dict["Median_Income"] = MEDIANINCOME
        medianincome_info.append(medianincome_dict)
    
    return jsonify(medianincome_info)



if __name__ == "__main__":
    app.run(debug=True)
