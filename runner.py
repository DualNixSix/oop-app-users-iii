from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser

# create one instance of each
user_alice = FreeUser(11, "Alice", "Aliceb@mail.com", 12345, "USA")
user_bob = PremiumUser(22, "Bob", "Boba@mail.com", 54321,"CAN")

user_karen = PremiumUser(33, "Karen", "Karenc@mail.com", 10987, "EUR")

user_linus = FreeUser(44, "Linus", "Linusb@mail.com", 65432, "ASIA")

user_alice.make_post("Hi")
user_alice.make_post()
user_alice.make_post()
user_bob.make_post()
user_bob.make_post()
user_bob.make_post()
user_karen.make_post()
user_karen.make_post()
user_karen.make_post()
user_linus.make_post()
user_linus.make_post()
user_linus.make_post()


print(FreeUser.all_posts)