from sqlalchemy import Column, Integer, String, SMALLINT, REAL, DATE, ForeignKey
from app import db

class Volcano(db.Model):
    namev = Column(String, primary_key=True)
    latitude = Column(REAL)
    longitude = Column(REAL)
    height = Column(SMALLINT)

    def __init__(self, namev, latitude, longitude, height):
        self.namev = namev
        self.latitude = latitude
        self.longitude = longitude
        self.height = height

class State_volcano(db.Model):
    ids = Column(Integer, primary_key=True)
    namev = Column(String, ForeignKey('volcano.namev', ondelete='CASCADE'))
    date_state = Column(DATE)
    thermal_anomaly = Column(SMALLINT)
    number_events = Column(SMALLINT)
    max_pgd_height = Column(SMALLINT)
    observ_ash_emissions = Column(String)
    hazard_code = Column(String)

    def __init__(self,namev, date_state, thermal_anomaly, number_events,
                 max_pgd_height, observ_ash_emissions, hazard_code):
        self.namev = namev
        self.date_state = date_state
        self.thermal_anomaly = thermal_anomaly
        self.number_events = number_events
        self.max_pgd_height = max_pgd_height
        self.observ_ash_emissions = observ_ash_emissions
        self.hazard_code = hazard_code
