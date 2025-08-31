# Healthcare360.in - Flask Web Application

A modern, responsive healthcare website built with Python Flask, featuring educational resources, preventive care information, curative support, and specialist consultations.

## Features

- **Educational Support**: Health education resources and knowledge base
- **Preventive Care**: Guidelines for healthy living and disease prevention
- **Curative Support**: Medical consultation and specialist referrals
- **City-based Services**: Location-specific healthcare information
- **Health Programs**: Educational webinars, workshops, and awareness campaigns
- **Medical Specialists**: Directory of healthcare professionals across specialties
- **Responsive Design**: Mobile-friendly interface using Tailwind CSS
- **Contact System**: User inquiry and feedback management

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Templates**: Jinja2 templating engine
- **Icons**: Font Awesome and custom SVG icons
- **Fonts**: Inter font family from Google Fonts

## Project Structure

```
healthcare_web/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── index.html       # Homepage
│   ├── contact.html     # Contact page
│   ├── programs.html    # Health programs page
│   └── specialists.html # Medical specialists page
└── static/              # Static assets (CSS, JS, images)
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download

Download the project files to your local machine.

### Step 2: Navigate to Project Directory

```bash
cd healthcare_web
```

### Step 3: Create Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
python app.py
```

The application will start running on `http://localhost:5000`

## Usage

### Homepage (`/`)
- Overview of healthcare services
- Educational, preventive, and curative sections
- City selection for localized information
- Health program dashboard

### Programs (`/programs`)
- Current and upcoming health education programs
- Program calendar and registration
- Webinar and workshop information

### Specialists (`/specialists`)
- Medical specialist directory
- Consultation information
- Emergency contact details

### Contact (`/contact`)
- Contact form for inquiries
- Company information
- Social media links

## API Endpoints

The application also provides REST API endpoints:

- `GET /api/cities` - List available cities
- `GET /api/programs` - List health programs
- `GET /api/specialists` - List medical specialists
- `POST /api/contact` - Submit contact form

## Customization

### Adding New Cities

Edit the `CITIES` list in `app.py`:

```python
CITIES = [
    {'id': 'newcity', 'name': 'New City', 'state': 'State Name'},
    # ... existing cities
]
```

### Adding New Health Programs

Edit the `HEALTH_PROGRAMS` list in `app.py`:

```python
HEALTH_PROGRAMS = [
    {
        'id': 4,
        'title': 'New Program Title',
        'type': 'Program Type',
        'date': '2025-01-01',
        'time': '10:00',
        'duration': '1 hour',
        'status': 'Upcoming'
    },
    # ... existing programs
]
```

### Adding New Specialists

Edit the `SPECIALISTS` list in `app.py`:

```python
SPECIALISTS = [
    {'area': 'New Specialty', 'status': 'Available', 'doctors': 'Dr. Name'},
    # ... existing specialists
]
```

## Development

### Running in Development Mode

The application runs in debug mode by default when you run `python app.py`. This enables:

- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

### Production Deployment

For production deployment, consider:

1. Setting `debug=False` in `app.py`
2. Using a production WSGI server like Gunicorn
3. Setting up proper environment variables
4. Implementing database integration
5. Adding user authentication
6. Setting up HTTPS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational and demonstration purposes.

## Support

For support or questions, please use the contact form on the website or create an issue in the repository.

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication and accounts
- Appointment booking system
- Real-time chat support
- Mobile app development
- Multi-language support
- Advanced search functionality
- Health record management
- Telemedicine integration
