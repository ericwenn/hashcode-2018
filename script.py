input = open("a_example.in", "r")

first = input.readline().split()

rows = int(first[0])
cols = int(first[1])
vehicles = int(first[2])
n_rides = int(first[3])
bonus = int(first[4])
steps = int(first[5])

rides = []

class Ride:

    def __init__(self, fro, to, start, end):
      self.start = start
      self.end = end
      self.fro = fro
      self.to = to

    def __str__( self ):
      return "Ride From: " + str(self.fro) + " To: " + str(self.to) + " Starting: " + str(self.start) + " Ending: " + str(self.end)

for line in input:
    lin = line.split()
    lin = list(map(lambda x: int(x), lin))
    rides.append(Ride((lin[0], lin[1]), (lin[2], lin[3]), lin[4], lin[5]))

print map(lambda x: str(x), rides)
