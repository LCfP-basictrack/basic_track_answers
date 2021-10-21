import matplotlib.pyplot as plt

latitudes = []
longitudes = []
elevations = []
with open("buren.csv") as gps_data:
    for gps_coordinate in gps_data.readlines():
        latitude, longitude, elevation = gps_coordinate.split(",")
        latitudes.append(float(latitude))
        longitudes.append(float(longitude))
        elevations.append(float(elevation))

figure = plt.figure(figsize=(48, 18))

axes = figure.add_subplot(2, 3, 2)
axes.plot(longitudes, latitudes)

axes = figure.add_subplot(2, 3, 4)
axes.plot(latitudes, elevations)

axes = figure.add_subplot(2, 3, 6)
axes.plot(longitudes, elevations)

axes = figure.add_subplot(2, 3, 5, projection="3d")
axes.plot(longitudes, latitudes, elevations)

plt.show()
