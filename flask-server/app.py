import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Nc1143618@localhost/email-scanner'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    date_entered = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def repr(self):
        return f"Event: {self.description}"
    
    def __init__(self, description):
        self.description = description

def format_event(event):
    return {
        'id': event.id,
        'description': event.description,
        'date_entered': event.date_entered
    }

@app.route('/')
def hello():
    return 'Hello, World!'

# Create event
@app.route('/events', methods=['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    return [format_event(event) for event in events]

def get_event(event_id):
    event = Event.query.get(event_id)
    return format_event(event)


@app.route('/events', method=['PUT'])
def update_event(event_id):
    event = Event.query.get(event_id)
    description = request.json['description']
    event.description = description
    db.session.commit()
    return format_event(event)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)