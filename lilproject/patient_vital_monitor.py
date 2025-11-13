class PatientMonitor:
    """Monitor patient vital signs."""
    
    def __init__(self, patient_name):
        self.patient_name = patient_name
        self.vitals_history = []
    
    def check_vitals_daily(self, days):
        """
        Record patient vitals for specified number of days.
        
        Uses FOR loop because we know exactly how many days to monitor.
        """
        print(f"Starting {days}-day vital monitoring for {self.patient_name}")
        print("="*50)
        
        for day in range(1, days + 1):
            # Simulate vital signs (in real app, would get from sensors)
            heart_rate = 70 + (day % 10)
            blood_pressure = f"{120 + day}/80"
            temperature = 98.6
            
            vital_record = {
                'day': day,
                'heart_rate': heart_rate,
                'blood_pressure': blood_pressure,
                'temperature': temperature
            }
            
            self.vitals_history.append(vital_record)
            
            print(f"Day {day}:")
            print(f"  Heart Rate: {heart_rate} bpm")
            print(f"  Blood Pressure: {blood_pressure} mmHg")
            print(f"  Temperature: {temperature}°F")
            print("-"*50)
        
        print(f"✓ Completed {days}-day monitoring\n")
        return self.vitals_history


# Example usage
monitor = PatientMonitor("John Smith")
vitals = monitor.check_vitals_daily(5)