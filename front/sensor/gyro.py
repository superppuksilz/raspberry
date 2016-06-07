import coordinate

class Gyro:
    coordSet = 0

    def __init__(self):
        coordSet = coordinate.Coordinate()
        
    def setCoord(self, x, y, z):
        coordSet.setCoordinate(x, y, z)
    def getCoord(self):
        return coordSet
    
