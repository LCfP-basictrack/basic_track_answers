import folium

coordinates = []
with open("buren.csv") as gps_data:
    for gps_coordinate in gps_data.readlines():
        latitude, longitude, _ = gps_coordinate.split(",")
        coordinates.append((float(latitude), float(longitude)))

center = (min(coordinates)[0] + max(coordinates)[0]) / 2, (min(coordinates)[1] + max(coordinates)[1]) / 2

route_map = folium.Map(location=[center[0], center[1]], zoom_start=15)
folium.PolyLine(coordinates).add_to(route_map)

route_map.save("route.html")
