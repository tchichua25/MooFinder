import webbrowser

lat = input('Latitude: ') #41.716328"
lon = input('Longitude: ') #"44.807572"

f = open('map.html','w')

message = """<html>
<head></head>
<body><img src="https://maps.googleapis.com/maps/api/staticmap?center={Latitude},{Longitude}&zoom=16&size=400x400&key=AIzaSyCulWGxPfpeztNupiVyzclTc27AZ8MZBXg"></body>
</html>"""

message = message.format(Latitude = lat, Longitude = lon)

f.write(message)
f.close()

filename = 'file:///home/pi/' + 'map.html'
webbrowser.open_new_tab(filename)
