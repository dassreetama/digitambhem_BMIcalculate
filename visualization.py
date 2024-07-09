import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_bmi_trends(records):
    timestamps = [datetime.strptime(record[1], '%Y-%m-%d %H:%M:%S') for record in records]
    bmis = [record[4] for record in records]
    
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, bmis, marker='o')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.title('BMI Trends Over Time')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
