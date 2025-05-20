# Bhaskar Garg's Portfolio Website

A modern, animated portfolio website showcasing professional projects and experiences.

## Features

- Responsive design with modern animations
- Project showcase with detailed information
- Interactive gallery
- Video integration
- Smooth scrolling and transitions
- Mobile-friendly interface

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
├── static/            # Static files
│   ├── css/          # CSS files
│   ├── js/           # JavaScript files
│   ├── images/       # Image assets
│   └── media/        # Media files (PDFs, videos)
└── templates/         # HTML templates
    ├── base.html     # Base template
    ├── index.html    # Home page
    ├── projects.html # Projects page
    └── about.html    # About page
```

## Technologies Used

- Flask (Python web framework)
- HTML5/CSS3
- JavaScript
- AOS (Animate On Scroll)
- Flask-Assets (Asset management)
- Responsive design principles

## License

This project is licensed under the MIT License. 