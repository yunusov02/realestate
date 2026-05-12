from .models import Utility, Nearby


class UtilityService:
    @classmethod
    def get_all_utilities(cls):
        return Utility.objects.all()
    
    @classmethod
    def get_utility(cls, utility_id):
        return Utility.objects.get(id=utility_id)
    
    @classmethod
    def create_utility(cls, data):
        utility = Utility.objects.create(**data)
        return utility
    
    @classmethod
    def update_utility(cls, utility_id, data):
        utility = Utility.objects.get(id=utility_id)
        for key, value in data.items():
            setattr(utility, key, value)
        utility.save()
        return utility
    
    @classmethod
    def delete_utility(cls, utility_id):
        utility = Utility.objects.get(id=utility_id)
        utility.delete()
        return utility
    
    
class NearbyService:
    @classmethod
    def get_all_nearbies(cls):
        return Nearby.objects.all()
    
    @classmethod
    def get_nearby(cls, nearby_id):
        return Nearby.objects.get(id=nearby_id)
    
    @classmethod
    def create_nearby(cls, data):
        nearby = Nearby.objects.create(**data)
        return nearby
    
    @classmethod
    def update_nearby(cls, nearby_id, data):
        nearby = Nearby.objects.get(id=nearby_id)
        for key, value in data.items():
            setattr(nearby, key, value)
        nearby.save()
        return nearby
    
    @classmethod
    def delete_nearby(cls, nearby_id):
        nearby = Nearby.objects.get(id=nearby_id)
        nearby.delete()
        return nearby