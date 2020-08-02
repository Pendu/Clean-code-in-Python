class ComplicatedNameSpace:
    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)
        return instance
class Namespace:
    accepted_values =("id_", "user", "location")

    def __init__(self, **data):
        accepted_data = {k:v for k,v in data.items() if k in self.accepted_values}
        self.__dict__.update(accepted_data)