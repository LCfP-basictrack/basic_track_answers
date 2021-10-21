import gpxpy

file_name = input("What .gpx file would you like to convert? (without .gpx) ")
with open(file_name + ".gpx") as gpx_file:
    gpx_data = gpxpy.parse(gpx_file)

coordinates = []
for track in gpx_data.tracks:
    for segment in track.segments:
        for point in segment.points:
            # print("lat: {} long: {} elev: {}"
            #       .format(point.latitude,
            #               point.longitude,
            #               point.elevation))
            coordinates.append((point.latitude,
                                point.longitude,
                                point.elevation))

with open(file_name + ".csv", 'w') as csv_file:
    for coordinate in coordinates:
        csv_file.write("{},{},{}\n".format(*coordinate))
