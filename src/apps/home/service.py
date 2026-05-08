from apps.home.models import Home


class HomeService:

    def __init__(self):
        self.test = None
        
        
    @classmethod
    def get_all_homes(cls):
        return Home.objects.all()


    @classmethod
    def get_home_by_id(cls, home_id):
        try:
            return Home.objects.get(id=home_id)
        except Home.DoesNotExist:
            return None
        
        
    @classmethod
    def create_home(cls, home: Home):
        home.save()
        return home
    
    @classmethod
    def update_home(cls, home: Home, **kwargs):
        for key, value in kwargs.items():
            setattr(home, key, value)
        home.save()
        return home
    
    

    @classmethod
    def delete_home(cls, home: Home):
        home.delete()