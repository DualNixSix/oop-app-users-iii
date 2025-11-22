class User:
    all_posts = []

    def __init__(self, uid, name, email, dl, country, user_post = None, post_count = 0):
        self.uid = f"{country}: 192.168.{uid}.{len(name)}"
        self.name = name
        self.email = email 
        self.dl = dl
        self.country = country 
        self.user_post = user_post
        self.post_count = post_count

    def __str__(self):
        return f"My Name is {self.name}"
    
    def make_post(self):
        self.post_count += 1
        self.user_post = input(f"{self.name}, Please enter your post: ")
        self.all_posts.append(f'{self.uid}: {self.user_post}')

