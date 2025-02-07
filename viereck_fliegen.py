from djitellopy import Tello

tello = Tello()

tello.connect() # Die Tellodrohne wird verbunden
Batteriezustand = tello.get_battery()

print ("Der Akku ist zu:" , Batteriezustand , "% geladen.")

tello.takeoff() # Tello hebt ab

def viereck_fliegen(kantenlaenge, radius): #Definition der Funktion viereck_fliegen
    for x in range(4):
        tello.move_forward(kantenlaenge)
        tello.rotate_clockwise(radius)

viereck_fliegen(50,90)


tello.land()

