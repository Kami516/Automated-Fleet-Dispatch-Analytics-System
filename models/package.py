class Package:
    def __init__(self,id,weight,destination,region,status=False):
        self.id = id
        self.weight = weight
        self.destination = destination
        self.status = status
        self.region = region
        