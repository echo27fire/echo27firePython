import pyswisseph as swe
from datetime import datetime
import tabulate

# Set the current date and time
now = datetime.now()

# Convert current date and time to Julian day
jd = swe.julday(now.year, now.month, now.day, now.hour + (now.minute/60) + (now.second/3600))

# List of planets
planets = [
    'Sun',
    'Moon',
    'Mercury',
    'Venus',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto'
]

# Get the astrological information for each planet and store it in a list of dictionaries
data = []
for i, planet in enumerate(planets):
    degree, speed, rflag = swe.calc_ut(jd, i)
    
    # Get the zodiac sign
    sign = int(degree / 30)
    signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    
    # Format degree within the zodiac sign
    degree_in_sign = degree - (sign * 30)
    
    data.append({
        "Planet": planet,
        "Speed": speed,
        "Incarnation": signs[sign],
        "Degree": degree_in_sign
    })

# Display the data in a table format
print(tabulate.tabulate(data, headers="keys"))
