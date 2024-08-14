#running out of time so used random location

import folium

m = folium.Map(location=[51.505, -0.09], zoom_start=13)

points = [
    [51.5, -0.09],
    [51.51, -0.1],
    [51.52, -0.12]
]

#the idea is get the edges of each area and fill the area with the predicted price,
# green for money
folium.Polygon(
    locations=points,
    color='green',        
    fill=True,           
    fill_color='blue',   
    fill_opacity=0.5     
).add_to(m)

m.save('map.html')