import webbrowser

lat = "41.716328"
lon = "44.807572"

f = open('map.html','w')

message = """<html>
<head></head>
<body><img src="https://maps.googleapis.com/maps/api/staticmap?center={Latitude},{Longitude}&zoom=12&size=400x400&key=AIzaSyCulWGxPfpeztNupiVyzclTc27AZ8MZBXg"></body>
</html>"""

new_message = message.format(Latitude = lon, Longitude = lat)

f.write(message)
f.close()

filename = 'file:///home/pi/' + 'map.html'
webbrowser.open_new_tab(filename)
