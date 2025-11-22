from users.User import User


class FreeUser(User):
    def __init__(self, uid, name, email, dl, country):
        super().__init__(uid, name, email, dl, country)

    def make_post(self):
        if self.post_count >= 2:
            print(f"{self.name}! Error: You can't post more than twice as a free user. Please upgrade for premium features.")
            return
        else:
            super().make_post()


