class Package:
    def __init__(self,id,weight,volume,destination,region,status=False):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.destination = destination
        self.status = status
        self.region = region

        self.cost = (5 * (1*self.weight) + (3*self.volume))
        