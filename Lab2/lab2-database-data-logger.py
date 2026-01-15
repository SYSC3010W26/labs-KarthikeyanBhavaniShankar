
import sqlite3
import time
from datetime import datetime
import random


conn = sqlite3.connect("sensorDB.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sensordata (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    humidity REAL,
    pressure REAL
)
""")
conn.commit()

print("Starting data logger (Ctrl+C to stop)...")

try:
    while True:
       
        timestamp = datetime.now().isoformat()
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(30.0, 70.0), 2)
        pressure = round(random.uniform(980.0, 1020.0), 2)

        
        cursor.execute("""
        INSERT INTO sensordata (timestamp, temperature, humidity, pressure)
        VALUES (?, ?, ?, ?)
        """, (timestamp, temperature, humidity, pressure))

        conn.commit()

        
        print(f"{timestamp} | T={temperature}°C H={humidity}% P={pressure} hPa")

        
        time.sleep(1)

except KeyboardInterrupt:
    print("\nData logging stopped by user.")

finally:
    conn.close()

