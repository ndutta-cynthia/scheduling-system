class SocialMediaApp:
    def __init__(self):
        # Initialize an empty dictionary to store followers.
        self.followers = {}

    def follow(self, follower_id, followed_id):
        """
        Adds a follower relationship between two users.
        :param follower_id: ID of the follower user.
        :param followed_id: ID of the user being followed.
        """
        if followed_id not in self.followers:
            self.followers[followed_id] = []
        self.followers[followed_id].append(follower_id)

    def get_followers(self, user_id):
        """
        Returns a list of followers for a given user.
        :param user_id: ID of the user.
        :return: List of follower IDs.
        """
        return self.followers.get(user_id, [])

    def unfollow(self, follower_id, followed_id):
        """
        Removes a follower relationship between two users.
        :param follower_id: ID of the follower user.
        :param followed_id: ID of the user being unfollowed.
        """
        if followed_id in self.followers:
            self.followers[followed_id].remove(follower_id)

# Example usage:
if __name__ == "__main__":
    app = SocialMediaApp()

    # User IDs (you can replace these with actual user IDs)
    user1_id = 1
    user2_id = 2

    # User 1 follows User 2
    app.follow(user1_id, user2_id)

    # Get User 2's followers
    followers_of_user2 = app.get_followers(user2_id)
    print(f"Followers of User 2: {followers_of_user2}")

    # User 1 unfollows User 2
    app.unfollow(user1_id, user2_id)

    # Get User 2's followers after unfollow
    followers_of_user2_after_unfollow = app.get_followers(user2_id)
    print(f"Followers of User 2 after unfollow: {followers_of_user2_after_unfollow}")
