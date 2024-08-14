#running out of time so used random location

import folium

m = folium.Map(location=[51.505, -0.09], zoom_start=13)

points = [
    [51.5, -0.09],
    [51.51, -0.1],
    [51.52, -0.12]
]

folium.PolyLine(
    locations=points,
    color='blue',
    weight=5,
    opacity=0.7 
).add_to(m)

m.save('map.html')