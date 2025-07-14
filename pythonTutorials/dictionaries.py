import random

tracks = ["Speed Trials", "Alameda", "Between the Bars", "Angeles"]

dict = {
    "song": tracks,
    "album": "Either/Or",
    "artist": "Elliott Smith",
}

randomTrack = random.choice(dict["song"])
print(randomTrack)