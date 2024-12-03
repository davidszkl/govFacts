class PoliticalEvent:
    '''Event related to an Entity, can be a new bill being introduced,
        a new vote, a law being passed, etc..
    '''
    def __init__(self, name, entity, type, *args, **kwargs):
        self.name = name
        self.entity = entity
        self.type = type
        