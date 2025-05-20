from flask import Flask, render_template, send_from_directory
import os
from datetime import datetime, timezone

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Project data structure
PROJECTS = {
    'fpga-air-quality': {
        'title': 'FPGA Air Quality Monitoring System',
        'subtitle': 'Advanced air quality monitoring with real-time data processing',
        'overview': 'An innovative air quality monitoring system implemented on FPGA that provides real-time data processing and analysis capabilities. The system integrates multiple sensors and provides a comprehensive solution for environmental monitoring.',
        'features': [
            'Real-time air quality data processing',
            'Custom FPGA architecture implementation',
            'Multi-sensor integration and calibration',
            'Data visualization and analysis dashboard',
            'Automated alert system for threshold violations'
        ],
        'technologies': [
            'VHDL/Verilog',
            'Xilinx FPGA',
            'Python for Data Analysis',
            'Web Interface',
            'IoT Sensors'
        ],
        'implementation': '''
            <p>The system was implemented using a modular approach:</p>
            <ol>
                <li>Sensor Interface Module: Handles data acquisition from multiple sensors</li>
                <li>Data Processing Unit: Implements real-time signal processing algorithms</li>
                <li>Control Logic: Manages system operations and sensor calibration</li>
                <li>Communication Interface: Enables data transfer to the monitoring station</li>
            </ol>
        ''',
        'results': '''
            <p>The implementation achieved significant results:</p>
            <ul>
                <li>40% improvement in data processing speed</li>
                <li>99.9% accuracy in air quality measurements</li>
                <li>Real-time monitoring with less than 1-second delay</li>
                <li>Successfully deployed in multiple locations</li>
            </ul>
        ''',
        'images': [
            {'path': 'media/FPGA_AIRQUALITY.pdf', 'alt': 'FPGA Air Quality System'},
            {'path': 'media/WhatsApp Image 2025-05-19 at 11.44.07_19d51ec9.jpg', 'alt': 'System Implementation'}
        ],
        'documents': [
            {'path': 'media/FPGA_AIRQUALITY.pdf', 'title': 'Project Report'},
            {'path': 'media/FPGA_AIRQUALITY.pdf', 'title': 'Technical Documentation'}
        ]
    },
    'covid-care': {
        'title': 'COVID Care System',
        'subtitle': 'Innovative healthcare solution for COVID-19 management',
        'overview': 'A comprehensive healthcare solution designed to manage COVID-19 cases effectively, providing real-time monitoring, resource management, and emergency response coordination.',
        'features': [
            'Patient monitoring system',
            'Healthcare resource management',
            'Emergency response coordination',
            'Data-driven decision support',
            'Automated alert system'
        ],
        'technologies': [
            'IoT Sensors',
            'Cloud Computing',
            'Data Analytics',
            'Mobile Application',
            'Web Interface'
        ],
        'implementation': '''
            <p>The system was developed with a focus on scalability and reliability:</p>
            <ol>
                <li>Patient Monitoring Module: Tracks vital signs and symptoms</li>
                <li>Resource Management System: Optimizes healthcare resource allocation</li>
                <li>Emergency Response Module: Coordinates rapid response to critical cases</li>
                <li>Analytics Dashboard: Provides insights for decision-making</li>
            </ol>
        ''',
        'results': '''
            <p>The system demonstrated significant impact:</p>
            <ul>
                <li>30% reduction in response time for critical cases</li>
                <li>Improved resource utilization by 45%</li>
                <li>Enhanced patient monitoring efficiency</li>
                <li>Successfully deployed in multiple healthcare facilities</li>
            </ul>
        ''',
        'images': [
            {'path': 'media/COVID CARE.pdf', 'alt': 'COVID Care System'},
            {'path': 'media/WhatsApp Image 2025-05-19 at 11.45.34_86180a3e.jpg', 'alt': 'System Interface'}
        ],
        'documents': [
            {'path': 'media/COVID CARE.pdf', 'title': 'Project Report'},
            {'path': 'media/COVID CARE.pdf', 'title': 'User Manual'}
        ]
    }
}

@app.context_processor
def inject_now():
    return {'now': datetime.now(timezone.utc)}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/technical')
def technical():
    return render_template('technical.html')

@app.route('/technical/work-experience')
def work_experience():
    return render_template('technical/work_experience.html',
        page_title="Work Experience",
        page_subtitle="Professional journey and achievements",
        back_url="/technical",
        back_text="Technical",
        main_content="""
            <p>My professional journey has been marked by continuous growth and impactful contributions across various roles. Each position has provided unique opportunities to develop both technical expertise and leadership skills.</p>
            <p>Key aspects of my work experience include:</p>
            <ul>
                <li>Leading technical teams and projects</li>
                <li>Implementing innovative solutions</li>
                <li>Driving process improvements</li>
                <li>Mentoring junior team members</li>
                <li>Collaborating with cross-functional teams</li>
            </ul>
        """,
        main_image={
            'path': 'images/work/overview.jpg',
            'alt': 'Professional Experience',
            'caption': 'Leading and innovating in the tech industry'
        },
        additional_sections=[
            {
                'title': 'Professional Roles',
                'subtitle': 'A timeline of my career progression',
                'type': 'list',
                'items': [
                    {
                        'icon': 'fas fa-briefcase',
                        'title': 'Senior Software Engineer',
                        'description': 'Led development of critical systems and mentored junior developers',
                        'subitems': [
                            {
                                'title': 'Key Achievements',
                                'description': 'Improved system performance by 40% through optimization'
                            },
                            {
                                'title': 'Technologies',
                                'description': 'Python, Django, React, AWS'
                            }
                        ]
                    }
                    # Add more roles here
                ]
            }
        ]
    )

@app.route('/technical/projects')
def projects():
    return render_template('technical/projects.html',
        page_title="Technical Projects",
        page_subtitle="Innovative solutions and technical achievements",
        back_url="/technical",
        back_text="Technical",
        main_content="""
            <p>My technical projects showcase my ability to solve complex problems and create innovative solutions. Each project represents a unique challenge and learning opportunity.</p>
            <p>Project highlights include:</p>
            <ul>
                <li>Full-stack web applications</li>
                <li>Machine learning implementations</li>
                <li>System architecture design</li>
                <li>Performance optimization</li>
                <li>Open-source contributions</li>
            </ul>
        """,
        main_image={
            'path': 'images/projects/overview.jpg',
            'alt': 'Technical Projects',
            'caption': 'Innovative solutions and technical achievements'
        }
    )

@app.route('/technical/internships')
def internships():
    return render_template('technical/internships.html',
        page_title="Internships",
        page_subtitle="Professional growth through industry experience",
        back_url="/technical",
        back_text="Technical",
        main_content="""
            <p>My internship experiences have been instrumental in developing both technical and professional skills. Each opportunity has provided valuable insights into industry practices and real-world problem-solving.</p>
            <p>Key learning areas include:</p>
            <ul>
                <li>Industry-standard development practices</li>
                <li>Team collaboration and communication</li>
                <li>Project management methodologies</li>
                <li>Technical problem-solving</li>
                <li>Professional networking</li>
            </ul>
        """,
        main_image={
            'path': 'images/internships/overview.jpg',
            'alt': 'Internship Experience',
            'caption': 'Professional growth through diverse industry experiences'
        }
    )

@app.route('/technical/inventions')
def inventions():
    return render_template('technical/inventions.html',
        page_title="Inventions",
        page_subtitle="Innovative solutions and creative problem-solving",
        back_url="/technical",
        back_text="Technical",
        main_content="""
            <p>My inventions represent creative solutions to real-world problems, combining technical expertise with innovative thinking. Each invention addresses a specific need or challenge.</p>
            <p>Invention categories include:</p>
            <ul>
                <li>Hardware innovations</li>
                <li>Software solutions</li>
                <li>Process improvements</li>
                <li>Technical tools</li>
                <li>Educational aids</li>
            </ul>
        """,
        main_image={
            'path': 'images/inventions/overview.jpg',
            'alt': 'Inventions',
            'caption': 'Innovative solutions and creative problem-solving'
        }
    )

@app.route('/technical/projects/<project_id>')
def project_detail(project_id):
    if project_id in PROJECTS:
        return render_template('technical/project_detail.html', project=PROJECTS[project_id])
    return "Project not found", 404

@app.route('/masti')
def masti():
    return render_template('masti.html')

@app.route('/masti/chess')
def chess():
    return render_template('masti/chess.html',
        page_title="Chess Journey",
        page_subtitle="Strategic thinking and competitive achievements",
        back_url="/masti",
        back_text="Masti",
        main_content="""
            <p>My chess journey has been a fascinating exploration of strategy, tactics, and mental discipline. Through competitive play and continuous learning, I've developed valuable skills that extend beyond the chessboard.</p>
            <p>Chess highlights include:</p>
            <ul>
                <li>Tournament achievements</li>
                <li>Strategic thinking development</li>
                <li>Problem-solving skills</li>
                <li>Mental discipline</li>
                <li>Community involvement</li>
            </ul>
        """,
        main_image={
            'path': 'images/chess/overview.jpg',
            'alt': 'Chess Journey',
            'caption': 'Strategic thinking and competitive achievements'
        }
    )

@app.route('/masti/poetry')
def poetry():
    return render_template('masti/poetry.html',
        page_title="Poetry",
        page_subtitle="Creative expression through words",
        back_url="/masti",
        back_text="Masti",
        main_content="""
            <p>Poetry has been my creative outlet, allowing me to express thoughts, emotions, and observations through carefully crafted words. Each poem represents a unique moment or perspective.</p>
            <p>Poetry themes include:</p>
            <ul>
                <li>Personal reflections</li>
                <li>Social observations</li>
                <li>Nature and beauty</li>
                <li>Emotional experiences</li>
                <li>Philosophical musings</li>
            </ul>
        """,
        main_image={
            'path': 'images/poetry/overview.jpg',
            'alt': 'Poetry Collection',
            'caption': 'Creative expression through words'
        }
    )

@app.route('/masti/co-curricular')
def co_curricular():
    return render_template('masti/co_curricular.html',
        page_title="Co-curricular Activities",
        page_subtitle="Beyond academics: leadership and personal growth",
        back_url="/masti",
        back_text="Masti",
        main_content="""
            <p>My co-curricular activities have played a crucial role in developing leadership skills, teamwork, and personal growth. These experiences have complemented my academic journey and shaped my overall development.</p>
            <p>Activity categories include:</p>
            <ul>
                <li>Leadership roles</li>
                <li>Community service</li>
                <li>Cultural activities</li>
                <li>Sports and fitness</li>
                <li>Event organization</li>
            </ul>
        """,
        main_image={
            'path': 'images/co_curricular/overview.jpg',
            'alt': 'Co-curricular Activities',
            'caption': 'Leadership and personal growth through diverse activities'
        }
    )

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects_page():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory('static/media', filename)

if __name__ == '__main__':
    app.run(debug=True) 