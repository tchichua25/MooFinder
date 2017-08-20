import webbrowser
import serial
import time
ser = serial.Serial("/dev/ttyACM0", baudrate = 115200)


def connection( a ): #function to connect arduino
    if a == 1:
        ser = serial.Serial("/dev/ttyACM0", baudrate = 115200)
        if ser.isOpen():
            print ("Connected to arduino \n") #for terminal [delete]
            return [1]
        else:
            return [0]
        
def coordinates ( a ): #function to find coordinates
    time.sleep(3) 
    if a == 1:
        data = ser.readline()
        b = data # to save data 
    return (b)

def stepup ( connect ):
    if connect == 1:
        marker = coordinates ( 1 )     # finds marker coordinates
    else:
        print 'no connection'

    coordinate = marker[:-2]    
    print 'Cordinates are ' + coordinate
    inp = input('Go on next step: ')
    if inp == 1:
        stepup2 (1, coordinate)
    else:
        stepup (1)

def stepup2 ( inp, coordinate):
    if inp == 1:
        zooming = input('Zoom: ')
        imageurl (coordinate, zooming);
    else:
        print 'Finding new location...'
        stepup (1);
        
def imageurl ( location, zooming ):
   key = 'AIzaSyCulWGxPfpeztNupiVyzclTc27AZ8MZBXg' #googl api key
   loc = location #coordinate into location
   zoom = zooming #area of the map
   url = 'https://maps.googleapis.com/maps/api/staticmap?center={Location}&zoom={Zoom}&size=800x320&key={APIkey}'
   url = url.format(Location = loc, Zoom = zoom, APIkey = key)
   print url
   browser (url)
   
def browser ( data ): # open the map in browser

    f = open('map.html','w')

    message = """<html>
    <head></head>
    <body><img src="{url}"></body>
    </html>"""

    message = message.format(url = data)

    f.write(message)
    f.close()

    filename = 'file:///home/pi/' + 'map.html'
    webbrowser.open_new_tab(filename)



connect = input('connect: ')       # asks to connect
connection ( connect );            # calls connection function
inp = stepup ( connect );                # next step to find location
#stepup2 ( connect );               # refind location/ display location


