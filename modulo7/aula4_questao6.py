import csv

file_path = 'spotify-2023.csv'
most_played_per_year = {}

with open(file_path, mode='r', encoding='latin-1') as file:
    reader = csv.reader(file)
    header = next(reader)  
    
    for row in reader:        
        if len(row) != len(header):
            continue
        if any('"' in cell for cell in row):
            continue        
        
        track_name = row[0]
        artist_name = row[1]
        released_year = row[3]
        streams = row[8]        
        
        if not (track_name and artist_name and released_year.isdigit() and streams.isdigit()):
            continue
        
        released_year = int(released_year)
        streams = int(streams)        
        
        if 2012 <= released_year <= 2022:
            if released_year not in most_played_per_year or streams > most_played_per_year[released_year][3]:
                most_played_per_year[released_year] = [track_name, artist_name, released_year, streams]


most_played_list = [most_played_per_year[year] for year in sorted(most_played_per_year)]


for item in most_played_list:
    print(item)
