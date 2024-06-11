# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt


#################################################
# Database Setup
#################################################
# Create the engine to the hawaii.sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
connection = engine.connect()

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#ROUTES - confirm queries use same variables as .ipynb file in part 1
# Stations route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in the data set
    most_recent = session.query(func.max(Measurement.date)).scalar()
    most_recent = dt.datetime.strptime(most_recent, '%Y-%m-%d')
    one_year_from = most_recent - dt.timedelta(days=365)

    # Query the last 12 months of precipitation data
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_from).\
        order_by(Measurement.date).all()

    # Convert query results to a dictionary
    precipitation_dict = {date: prcp for date, prcp in precipitation_data}

    return jsonify(precipitation_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    stations_data = session.query(Station.station).all()

    # Convert the query results to a list
    stations_list = [station[0] for station in stations_data]

    return jsonify(stations_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year from the last date in the data set
    most_recent = session.query(func.max(Measurement.date)).scalar()
    most_recent = dt.datetime.strptime(most_recent, '%Y-%m-%d')
    one_year_from = most_recent - dt.timedelta(days=365)

    # Find the most active station
    most_active_station_id = session.query(Measurement.station, func.count(Measurement.station).label('count')).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()[0]

    # Query the last 12 months of temperature observation data for the most active station
    temperature_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == most_active_station_id).\
        filter(Measurement.date >= one_year_from).\
        order_by(Measurement.date).all()

    # Convert the query results to a list of temperatures
    temperature_list = [temp for date, temp in temperature_data]

    return jsonify(temperature_list)

# Start and Start-End route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_stats(start, end=None):
    # Create the query for the temperature statistics
    if end:
        results = session.query(
            func.min(Measurement.tobs).label('min_temp'),
            func.avg(Measurement.tobs).label('avg_temp'),
            func.max(Measurement.tobs).label('max_temp')
        ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    else:
        results = session.query(
            func.min(Measurement.tobs).label('min_temp'),
            func.avg(Measurement.tobs).label('avg_temp'),
            func.max(Measurement.tobs).label('max_temp')
        ).filter(Measurement.date >= start).all()

    # Convert the query results to a dictionary
    temperature_stats = {
        "TMIN": results[0].min_temp,
        "TAVG": results[0].avg_temp,
        "TMAX": results[0].max_temp
    }

    return jsonify(temperature_stats)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)