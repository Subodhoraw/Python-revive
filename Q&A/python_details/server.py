"""
PYTHON WEB SERVERS: COMPLETE GUIDE
===================================

This guide covers:
1. Flask - Simple, flexible web framework
2. FastAPI - Modern, fast (async) API framework
3. Database integration (SQLite, PostgreSQL)
4. RESTful APIs
5. Authentication
6. Real-world applications

Installation:
pip install flask fastapi uvicorn sqlalchemy pydantic
"""

# ============================================================================
# PART 1: FLASK BASICS
# ============================================================================

print("="*80)
print("PART 1: FLASK - SIMPLE WEB SERVER")
print("="*80)

from flask import Flask, request, jsonify, render_template_string
import sqlite3
from datetime import datetime
import json

# Create Flask application
app = Flask(__name__)

# ============================================================================
# BASIC ROUTES
# ============================================================================

@app.route('/')
def home():
    """Home page."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hospital Management System</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                max-width: 800px; 
                margin: 50px auto;
                padding: 20px;
                background: #f5f5f5;
            }
            .card {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            h1 { color: #2c3e50; }
            .endpoint {
                background: #ecf0f1;
                padding: 10px;
                margin: 10px 0;
                border-left: 4px solid #3498db;
            }
            .method {
                display: inline-block;
                padding: 4px 8px;
                border-radius: 4px;
                font-weight: bold;
                margin-right: 10px;
            }
            .get { background: #27ae60; color: white; }
            .post { background: #3498db; color: white; }
            .put { background: #f39c12; color: white; }
            .delete { background: #e74c3c; color: white; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🏥 Hospital Management API</h1>
            <p>Welcome to the Hospital Management System API</p>
        </div>
        
        <div class="card">
            <h2>Available Endpoints:</h2>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/patients</code> - Get all patients
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/patients/&lt;id&gt;</code> - Get specific patient
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <code>/api/patients</code> - Create new patient
            </div>
            
            <div class="endpoint">
                <span class="method put">PUT</span>
                <code>/api/patients/&lt;id&gt;</code> - Update patient
            </div>
            
            <div class="endpoint">
                <span class="method delete">DELETE</span>
                <code>/api/patients/&lt;id&gt;</code> - Delete patient
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/api/appointments</code> - Get all appointments
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <code>/api/appointments</code> - Create appointment
            </div>
        </div>
        
        <div class="card">
            <h2>Example Usage:</h2>
            <pre style="background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 4px;">
# Get all patients
curl http://localhost:5000/api/patients

# Create new patient
curl -X POST http://localhost:5000/api/patients \\
  -H "Content-Type: application/json" \\
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": "1985-05-15",
    "gender": "Male",
    "phone": "555-1234"
  }'
            </pre>
        </div>
    </body>
    </html>
    """
    return html

# ============================================================================
# DATABASE SETUP
# ============================================================================

def init_db():
    """Initialize SQLite database."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    # Patients table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth DATE,
        gender TEXT,
        phone TEXT,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Appointments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_name TEXT,
        appointment_date DATE,
        appointment_time TEXT,
        reason TEXT,
        status TEXT DEFAULT 'Scheduled',
        FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
    )
    ''')
    
    conn.commit()
    conn.close()

# Initialize database when module loads
init_db()

# ============================================================================
# PATIENT API ENDPOINTS (CRUD)
# ============================================================================

@app.route('/api/patients', methods=['GET'])
def get_patients():
    """Get all patients."""
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients')
    patients = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({
        'success': True,
        'count': len(patients),
        'data': patients
    })

@app.route('/api/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    """Get specific patient."""
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    patient = cursor.fetchone()
    
    conn.close()
    
    if patient:
        return jsonify({
            'success': True,
            'data': dict(patient)
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Patient not found'
        }), 404

@app.route('/api/patients', methods=['POST'])
def create_patient():
    """Create new patient."""
    data = request.get_json()
    
    # Validate required fields
    required = ['first_name', 'last_name']
    if not all(field in data for field in required):
        return jsonify({
            'success': False,
            'error': 'Missing required fields'
        }), 400
    
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone, email)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data.get('first_name'),
        data.get('last_name'),
        data.get('date_of_birth'),
        data.get('gender'),
        data.get('phone'),
        data.get('email')
    ))
    
    patient_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'message': 'Patient created successfully',
        'patient_id': patient_id
    }), 201

@app.route('/api/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    """Update patient."""
    data = request.get_json()
    
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    # Build dynamic UPDATE query
    fields = []
    values = []
    
    for field in ['first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'email']:
        if field in data:
            fields.append(f"{field} = ?")
            values.append(data[field])
    
    if not fields:
        return jsonify({
            'success': False,
            'error': 'No fields to update'
        }), 400
    
    values.append(patient_id)
    query = f"UPDATE patients SET {', '.join(fields)} WHERE patient_id = ?"
    
    cursor.execute(query, values)
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({
            'success': False,
            'error': 'Patient not found'
        }), 404
    
    conn.close()
    
    return jsonify({
        'success': True,
        'message': 'Patient updated successfully'
    })

@app.route('/api/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    """Delete patient."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM patients WHERE patient_id = ?', (patient_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        conn.close()
        return jsonify({
            'success': False,
            'error': 'Patient not found'
        }), 404
    
    conn.close()
    
    return jsonify({
        'success': True,
        'message': 'Patient deleted successfully'
    })

# ============================================================================
# APPOINTMENT API ENDPOINTS
# ============================================================================

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    """Get all appointments."""
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT a.*, p.first_name, p.last_name
    FROM appointments a
    JOIN patients p ON a.patient_id = p.patient_id
    ORDER BY a.appointment_date, a.appointment_time
    ''')
    
    appointments = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify({
        'success': True,
        'count': len(appointments),
        'data': appointments
    })

@app.route('/api/appointments', methods=['POST'])
def create_appointment():
    """Create new appointment."""
    data = request.get_json()
    
    required = ['patient_id', 'doctor_name', 'appointment_date', 'appointment_time']
    if not all(field in data for field in required):
        return jsonify({
            'success': False,
            'error': 'Missing required fields'
        }), 400
    
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO appointments (patient_id, doctor_name, appointment_date, 
                            appointment_time, reason)
    VALUES (?, ?, ?, ?, ?)
    ''', (
        data['patient_id'],
        data['doctor_name'],
        data['appointment_date'],
        data['appointment_time'],
        data.get('reason', '')
    ))
    
    appointment_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({
        'success': True,
        'message': 'Appointment created successfully',
        'appointment_id': appointment_id
    }), 201

# ============================================================================
# SEARCH AND FILTER ENDPOINTS
# ============================================================================

@app.route('/api/patients/search', methods=['GET'])
def search_patients():
    """Search patients by name."""
    query = request.args.get('q', '')
    
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM patients 
    WHERE first_name LIKE ? OR last_name LIKE ?
    ''', (f'%{query}%', f'%{query}%'))
    
    patients = [dict(row) for row in cursor.fetchall()]
    conn.close()
    
    return jsonify({
        'success': True,
        'query': query,
        'count': len(patients),
        'data': patients
    })

# ============================================================================
# STATISTICS ENDPOINT
# ============================================================================

@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """Get hospital statistics."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    # Total patients
    cursor.execute('SELECT COUNT(*) FROM patients')
    total_patients = cursor.fetchone()[0]
    
    # Total appointments
    cursor.execute('SELECT COUNT(*) FROM appointments')
    total_appointments = cursor.fetchone()[0]
    
    # Appointments today
    cursor.execute('''
    SELECT COUNT(*) FROM appointments 
    WHERE appointment_date = date('now')
    ''')
    appointments_today = cursor.fetchone()[0]
    
    # Patients by gender
    cursor.execute('''
    SELECT gender, COUNT(*) as count 
    FROM patients 
    GROUP BY gender
    ''')
    gender_stats = [{'gender': row[0], 'count': row[1]} 
                   for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({
        'success': True,
        'statistics': {
            'total_patients': total_patients,
            'total_appointments': total_appointments,
            'appointments_today': appointments_today,
            'gender_distribution': gender_stats
        }
    })

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

# ============================================================================
# RUN FLASK SERVER
# ============================================================================

def run_flask_server():
    """Run Flask development server."""
    print("\n" + "="*80)
    print("FLASK SERVER STARTING")
    print("="*80)
    print("\n🚀 Server running at: http://localhost:5000")
    print("\n📚 API Documentation: http://localhost:5000")
    print("\n🔧 Available Endpoints:")
    print("  GET    /api/patients")
    print("  GET    /api/patients/<id>")
    print("  POST   /api/patients")
    print("  PUT    /api/patients/<id>")
    print("  DELETE /api/patients/<id>")
    print("  GET    /api/appointments")
    print("  POST   /api/appointments")
    print("  GET    /api/patients/search?q=<query>")
    print("  GET    /api/statistics")
    print("\n💡 Test with curl or Postman")
    print("\nPress CTRL+C to stop the server")
    print("="*80 + "\n")
    
    app.run(debug=True, port=5000)


# ============================================================================
# PART 2: FASTAPI (MODERN ASYNC FRAMEWORK)
# ============================================================================

print("\n" + "="*80)
print("PART 2: FASTAPI - MODERN ASYNC WEB SERVER")
print("="*80)

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date

# Create FastAPI application
fastapi_app = FastAPI(
    title="Hospital Management API",
    description="Modern async API for hospital management",
    version="1.0.0"
)

# ============================================================================
# PYDANTIC MODELS (DATA VALIDATION)
# ============================================================================

class PatientCreate(BaseModel):
    """Model for creating a patient."""
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: Optional[date] = None
    gender: Optional[str] = Field(None, max_length=20)
    phone: Optional[str] = Field(None, max_length=20)
    email: Optional[str] = Field(None, max_length=100)
    
    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "date_of_birth": "1985-05-15",
                "gender": "Male",
                "phone": "555-1234",
                "email": "john.doe@email.com"
            }
        }

class PatientResponse(BaseModel):
    """Model for patient response."""
    patient_id: int
    first_name: str
    last_name: str
    date_of_birth: Optional[date]
    gender: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    created_at: str

class AppointmentCreate(BaseModel):
    """Model for creating appointment."""
    patient_id: int
    doctor_name: str
    appointment_date: date
    appointment_time: str
    reason: Optional[str] = None

# ============================================================================
# FASTAPI ENDPOINTS
# ============================================================================

@fastapi_app.get("/", response_class=HTMLResponse)
async def fastapi_home():
    """FastAPI home page with auto-generated docs."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hospital Management API - FastAPI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            }
            h1 { color: #667eea; margin: 0 0 10px 0; }
            .badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                background: #667eea;
                color: white;
                font-size: 12px;
                font-weight: bold;
            }
            .docs-link {
                display: inline-block;
                margin: 20px 10px 0 0;
                padding: 12px 24px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                font-weight: bold;
            }
            .docs-link:hover {
                background: #5568d3;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🏥 Hospital Management API</h1>
            <span class="badge">FastAPI v1.0.0</span>
            
            <p style="margin-top: 20px;">
                Modern, fast (high-performance) API built with FastAPI.
            </p>
            
            <h3>✨ Features:</h3>
            <ul>
                <li>🚀 High performance (async/await)</li>
                <li>📝 Automatic API documentation</li>
                <li>✅ Data validation with Pydantic</li>
                <li>🔍 Type hints everywhere</li>
                <li>📊 OpenAPI/Swagger integration</li>
            </ul>
            
            <div>
                <a href="/docs" class="docs-link">📚 Interactive API Docs (Swagger)</a>
                <a href="/redoc" class="docs-link">📖 API Documentation (ReDoc)</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@fastapi_app.get("/api/patients", response_model=List[PatientResponse])
async def fastapi_get_patients():
    """Get all patients (FastAPI version)."""
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients')
    patients = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return patients

@fastapi_app.post("/api/patients", response_model=dict, status_code=201)
async def fastapi_create_patient(patient: PatientCreate):
    """Create new patient (FastAPI version with validation)."""
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO patients (first_name, last_name, date_of_birth, gender, phone, email)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        patient.first_name,
        patient.last_name,
        patient.date_of_birth,
        patient.gender,
        patient.phone,
        patient.email
    ))
    
    patient_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {
        "success": True,
        "message": "Patient created successfully",
        "patient_id": patient_id
    }

@fastapi_app.get("/api/patients/{patient_id}", response_model=PatientResponse)
async def fastapi_get_patient(patient_id: int):
    """Get specific patient (FastAPI version)."""
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM patients WHERE patient_id = ?', (patient_id,))
    patient = cursor.fetchone()
    
    conn.close()
    
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return dict(patient)

# ============================================================================
# RUN FASTAPI SERVER
# ============================================================================

def run_fastapi_server():
    """Run FastAPI server with uvicorn."""
    import uvicorn
    
    print("\n" + "="*80)
    print("FASTAPI SERVER STARTING")
    print("="*80)
    print("\n🚀 Server running at: http://localhost:8000")
    print("\n📚 Interactive API Docs: http://localhost:8000/docs")
    print("📖 Alternative Docs: http://localhost:8000/redoc")
    print("\n✨ Features:")
    print("  • Automatic data validation")
    print("  • Interactive API documentation")
    print("  • Async/await support")
    print("  • OpenAPI/Swagger integration")
    print("\nPress CTRL+C to stop the server")
    print("="*80 + "\n")
    
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*80)
    print("PYTHON WEB SERVERS - CHOOSE YOUR FRAMEWORK")
    print("="*80)
    print("\n1. Flask - Simple, flexible (http://localhost:5000)")
    print("2. FastAPI - Modern, fast with auto-docs (http://localhost:8000)")
    print("\nBoth servers use the same SQLite database (hospital.db)")
    
    choice = input("\nWhich server do you want to run? (1/2): ").strip()
    
    if choice == '1':
        run_flask_server()
    elif choice == '2':
        run_fastapi_server()
    else:
        print("\n❌ Invalid choice. Please run again and select 1 or 2.")
        
    print("\n\n" + "="*80)
    print("SERVER STOPPED")
    print("="*80)