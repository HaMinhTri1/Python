class Youtube:
    def __init__(self, username, subscribers=0, subcriptions=0):
        self.username = username
        self.subcribers =  subscribers
        self.subcriptions = subcriptions
    def subscribe(self, user):
        user.subcribers +=1
        user.subcriptions +=1
        
user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user1.subscribe(user2)
user2.subscribe(user1)
print(f"User 1 subscribers: {user1.subcribers}")
print(f"User 1 subscriptions: {user1.subcriptions}")
print(f"User 2 subscribers: {user2.subcribers}")
print(f"User 2 subscriptions: {user2.subcriptions}")
