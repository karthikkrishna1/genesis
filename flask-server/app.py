import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

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
    events_list = [format_event(event) for event in events]
    return {'events': events_list}


# Get event by id
@app.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    return {'event': format_event(event)}

# Update event by id
@app.route('/events/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description=description, date_entered=datetime.now()))
    db.session.commit()
    return {'event': format_event(event.one())}

# Delete event by id
@app.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {id}) was successfully deleted'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)