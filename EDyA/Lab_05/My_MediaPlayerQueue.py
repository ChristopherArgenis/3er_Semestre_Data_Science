from random import randint
class track(object):
  def __init__(self, title=None):
    self.title = title
    self.length = randint(5, 10)

# track1 = track("white whistle")
# track2 = track("butter butter")
# print(track1.length)
# print(track2.length)

import time
class MediaPlayerQueue(Queue):
  def __init__(self):
    super(MediaPlayerQueue, self).__init__()
  def add(self, track):
    self.enqueue(track)
  def play(self):
    while self.count > 0:
      current_track_node = self.dequeue()
      print("Now playing {}".format(current_track_node.title))
      time.sleep(current_track_node.length)

track1 = track("Lost on you")
track2 = track("All The Stars")
track3 = track("SO TIRED (Slowed)")
track4 = track("Congratulations (Post Malone)")
track5 = track("My eyes (Travis Scott)")

print("Tiempo aleatorio ligado a la cancion:")
print("-"*25)
print(f"La duracion aleatoria de {track1.title} es: {track1.length}s")
print(f"La duracion aleatoria de {track2.title} es: {track2.length}s")
print(f"La duracion aleatoria de {track3.title} es: {track3.length}s")
print(f"La duracion aleatoria de {track4.title} es: {track4.length}s")
print(f"La duracion aleatoria de {track5.title} es: {track5.length}s")
print("-"*25)
# Creacion de un Objeto MediaPlayerQueue
media_player = MediaPlayerQueue()

# Se añaden las canciones al objecto (Uso de cola)
media_player.add(track1)
media_player.add(track2)
media_player.add(track3)
media_player.add(track4)
media_player.add(track5)

# Se inician las canciones
media_player.play()