from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'healthcare360_secret_key_2025'

# Sample data for the healthcare website
CITIES = [
    {'id': 'lucknow', 'name': 'Lucknow', 'state': 'Uttar Pradesh'},
    {'id': 'raebareli', 'name': 'Raebareli', 'state': 'Uttar Pradesh'},
    {'id': 'noida', 'name': 'Noida', 'state': 'Uttar Pradesh'},
    {'id': 'delhi', 'name': 'Delhi', 'state': 'Delhi'},
    {'id': 'mumbai', 'name': 'Mumbai', 'state': 'Maharashtra'}
]

HEALTH_PROGRAMS = [
    {
        'id': 1,
        'title': 'Understanding Diabetes Management',
        'type': 'Online Webinar',
        'date': '2025-07-10',
        'time': '15:00',
        'duration': '2 hours',
        'status': 'Current Session'
    },
    {
        'id': 2,
        'title': 'First Aid for Common Emergencies',
        'type': 'Community Workshop',
        'date': '2025-07-12',
        'time': '10:00',
        'duration': '3 hours',
        'status': 'Upcoming'
    },
    {
        'id': 3,
        'title': 'Monsoon Health & Hygiene',
        'type': 'Awareness Campaign',
        'date': '2025-07-01',
        'time': 'Ongoing',
        'duration': '2 weeks',
        'status': 'Active'
    }
]

SPECIALISTS = [
    {'area': 'Surgery', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Cardiac', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Neuro', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Dental', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Dermatology', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Gastroenterology', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Orthopedic', 'status': 'Available', 'doctors': 'Panel Doctors'},
    {'area': 'Naturopathy', 'status': 'Available', 'doctors': 'Dr. Misbah'}
]

@app.route('/')
def index():
    return render_template('index.html', 
                         cities=CITIES, 
                         health_programs=HEALTH_PROGRAMS,
                         specialists=SPECIALISTS)

@app.route('/city/<city_id>')
def city_info(city_id):
    city = next((c for c in CITIES if c['id'] == city_id), None)
    if not city:
        flash('City not found', 'error')
        return redirect(url_for('index'))
    
    # In a real app, you would fetch city-specific data from a database
    city_data = {
        'hospitals': [
            {'name': f'{city["name"]} General Hospital', 'type': 'Government', 'rating': 4.2},
            {'name': f'{city["name"]} Medical Center', 'type': 'Private', 'rating': 4.5}
        ],
        'pharmacies': [
            {'name': f'{city["name"]} Pharmacy', 'location': 'City Center'},
            {'name': f'{city["name"]} Medical Store', 'location': 'Market Area'}
        ]
    }
    
    return render_template('city.html', city=city, city_data=city_data)

@app.route('/programs')
def programs():
    return render_template('programs.html', health_programs=HEALTH_PROGRAMS)

@app.route('/specialists')
def specialists():
    return render_template('specialists.html', specialists=SPECIALISTS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            # In a real app, you would save this to a database or send an email
            flash('Thank you for your message! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html')

@app.route('/api/cities')
def api_cities():
    return jsonify(CITIES)

@app.route('/api/programs')
def api_programs():
    return jsonify(HEALTH_PROGRAMS)

@app.route('/api/specialists')
def api_specialists():
    return jsonify(SPECIALISTS)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    
    if name and email and message:
        # In a real app, you would save this to a database or send an email
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    else:
        return jsonify({'success': False, 'message': 'Please fill in all fields.'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
