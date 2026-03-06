class Package:
    def __init__(self,id,weight,volume,destination,region,status=False):
        self.id = id
        self.weight = weight
        self.volume = volume
        self.destination = destination
        self.status = status
        self.region = region

        self.cost = round((15 + (8*self.weight) + (10*self.volume)),2)
        