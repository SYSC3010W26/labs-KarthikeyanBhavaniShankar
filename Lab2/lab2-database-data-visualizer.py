import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../sensorDB.db")
query = "SELECT * FROM sensordata"
df = pd.read_sql_query(query, conn)

conn.close()

df["timestamp"] = pd.to_datetime(df["timestamp"])
plt.figure(figsize=(10, 6))

plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)")
plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)")
plt.plot(df["timestamp"], df["pressure"], label="Pressure (hPa)")

plt.xlabel("Time")
plt.ylabel("Sensor Values")
plt.title("Sensor Data Over Time")
plt.legend()
plt.grid(True)
plt.savefig("lab2-database-plot.png")
plt.show()
