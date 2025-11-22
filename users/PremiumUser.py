from users.User import User


class PremiumUser(User):
    def __init__(self, uid, name, email, dl, country):
        super().__init__(uid, name, email, dl, country)
        
    pass

    