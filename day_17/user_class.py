class User:
    def __init__(self, user_id, username) -> None:
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        self.follow_list = []

    def follow(self, user):
        user.followers += 1
        self.following += 1
        self.follow_list.append(user)
    


def main() -> None:

    user_range = range(1, 6)

    users = [User(f"00{i}", f"user{i}") for i in user_range]

    for i in range(len(users)):
        if i < len(users) - 1:
            users[i].follow(users[i + 1])
            users[i + 1].follow(users[i]) 

    for user in users:
        print(f"{user.username} is following: {', '.join(u.username for u in user.follow_list)}")


main()