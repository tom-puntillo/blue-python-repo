import statistics

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]
    
flight_to_rome = 0
flight_times = []


for city in connections:
    if 'Rome' in city[1]:
        flight_to_rome += 1
        
        

for city in connections:
    if 'Rome' in city[1]:
      flight_times.append(city[2])
      

      
print(flight_to_rome, 'connections lead to Rome with an average flight time of', float(statistics.mean(flight_times)), 'minutes')