from djitellopy import Tello

drohne = Tello()
drohne.connect() #verbindet die Drohne mit dem Laptop
drohne.enable_mission_pads() #aktiviert die Missionpads

batterieladung = drohne.get_battery() #ermittelt die ladung der Batterie

print (f"Der Akku der Drohne ist zu {batterieladung} % geladen" )
drohne.takeoff() # Drohne startet

drohne.move_forward(100) # die Drohne fliegt 100cm nach vorne
drohne.set_video_direction(drohne.CAMERA_DOWNWARD) # die abwärtsgerichtete kamera wird eingeschaltet

ID = drohne.get_mission_pad_id() # legt die ID Variable fest
# Abfrage nach den Missionpad 
if ID == 4:
    print (f"Ich habe das Mission Pad mit der {ID} gefunden")
else:
    print(f"Aktuelle ID des erkannten Mission Pads lautet: {ID}")

drohne.rotate_clockwise(180)
drohne.move_forward(100)
drohne.land()

