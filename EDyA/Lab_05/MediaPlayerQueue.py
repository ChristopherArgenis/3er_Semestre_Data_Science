# Introduce the code of Queue in set with it.
from random import randint
class track(object):
  def __init__(self, title=None):
    self.title = title
    self.length = randint(5, 10)

track1 = track("white whistle")
track2 = track("butter butter")
print(track1.length)
print(track2.length)

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

track1 = track("white whistle")
track2 = track("butter butter")
track3 = track("Oh black star")
track4 = track("Watch that chicken")
track5 = track("Don't go")
media_player = MediaPlayerQueue()

media_player.add(track1)
media_player.add(track2)
media_player.add(track3)
media_player.add(track4)
media_player.add(track5)
media_player.play()