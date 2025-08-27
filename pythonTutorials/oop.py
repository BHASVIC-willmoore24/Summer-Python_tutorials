# Everything in python is an object

class Album:
    def play(self): # self points to current object instance
        print("music plays")

class Vinyl(Album): # Vinyl inherits Album
     def __init__(self, title, artist): #constructor
        self.title = title
        self.artist = artist


abbey_road = Vinyl("Abbey Road", "The Beatles")

print(abbey_road.title)
print(abbey_road.artist)
abbey_road.play()
