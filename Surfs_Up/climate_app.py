# imports
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine=engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station


# Flask setup
climate = Flask(__name__)

# Flask routes
@climate.route("/")
def home():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@climate.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    date = session.query(measurement.date).filter(measurement.date >= '2016-08-23').order_by(measurement.date).all()
    precipitation = session.query(measurement.prcp).filter(measurement.date >= '2016-08-23').order_by(measurement.date).all()
    




@climate.route("/api/v1.0/stations")
def stations():


@climate.route("/api/v1.0/tobs")
def tobs():


@climate.route("/api/v1.0/<start>")
def start():


@climate.route("/api/v1.0/<start>/<end>")
def end():