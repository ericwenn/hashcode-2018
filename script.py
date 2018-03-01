import math

file = "e_high_bonus.in"

input = open(file, "r")

first = input.readline().split()

rows = int(first[0])
cols = int(first[1])
vehicles = int(first[2])
n_rides = int(first[3])
bonus = int(first[4])
steps = int(first[5])

rides = []
veh = []

class Ride:

    def __init__(self, fro, to, start, end, _id):
      self.start = start
      self.end = end
      self.fro = fro
      self.to = to
      self.taken = False
      self.id = _id

    def __str__( self ):
      return "Ride " + str(self.id) + " From: " + str(self.fro) + " To: " + str(self.to) + " Starting: " + str(self.start) + " Ending: " + str(self.end)

i = 0
for line in input:
    lin = line.split()
    lin = list(map(lambda x: int(x), lin))
    rides.append(Ride((lin[0], lin[1]), (lin[2], lin[3]), lin[4], lin[5], i))
    i += 1

#print map(lambda x: str(x), rides)

for i in range(0, vehicles):
    veh.append({
        "rides": [],
        "step": 0,
        "pos": (0,0)
    })

def criterion(ride, veh):
    return dist(ride.fro, veh["pos"]) + ride.end

def points(ride, veh):
    p = dist(ride.fro, ride.to)
    if (dist(ride.fro, veh["pos"]) + veh["step"] < ride.start):
        p += bonus
    return p


def worthless(ride, veh):
    #print ride, veh
    return ride.end <= dist(ride.fro, veh["pos"]) + dist(ride.fro, ride.to) + veh["step"]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def time(ride, veh):
    return max(dist(ride.fro, veh["pos"]) + veh["step"], ride.start) + dist(ride.fro, ride.to)

for v in veh:
    while (v["step"] < steps):
        min = 100000000
        minIndex = None

        for i in range(0, len(rides)):

            #print worthless(rides[i], v)

            if (worthless(rides[i], v)):
                continue



            if (criterion(rides[i], v) < min):
                min = criterion(rides[i], v)
                minIndex = i

        #print min, minIndex

        if (minIndex == None):
            break

        v["rides"].append(rides[minIndex].id)
        v["step"] += time(rides[minIndex], v)
        v["pos"] = rides[minIndex].to
        rides.pop(minIndex)

print veh

output = ""

for v in veh:
    output += str(len(v["rides"])) + " " + " ".join(map(lambda x: str(x), v["rides"])) + "\n"

_output = open("out_" + file, "w")
_output.write(output)
