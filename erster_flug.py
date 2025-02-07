from djitellopy import Tello

tello = Tello()

tello.connect() # Die Tellodrohne wird verbunden
Batteriezustand = tello.get_battery()

print ("Der Akku ist zu:" , Batteriezustand , "% geladen.")

tello.takeoff() # Die Drohne habt ab
tello.move_forward(80)
tello.land()



