from datetime import datetime, timedelta
def get_time_delta(minutes):
    return timedelta(minutes=minutes)
def get_current_time():
    return datetime.now()
def get_current_time_plus_minutes(minutes):
    return datetime.now() + timedelta(minutes=minutes)