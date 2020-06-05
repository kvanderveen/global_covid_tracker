from app import st
from datetime import datetime
from dateutil import tz


def current_date():
    date = datetime.utcnow().replace(tzinfo=tz.gettz('UTC')).astimezone(
        tz.gettz('America/Denver'))
    date_str = date.strftime('%B %d, %Y')
    return date_str


def page_header():
    st.title('Global COVID Tracker')
    date_str = current_date()
    st.subheader(date_str)
