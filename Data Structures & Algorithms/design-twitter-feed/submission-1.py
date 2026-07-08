class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((-self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_followers = self.followMap[userId]
        all_followers.add(userId)
        min_heap = []
        print(all_followers)
        for user in all_followers:
            tweets = self.tweetMap[user]
            for tweet in tweets:
                heapq.heappush(min_heap, tweet)
                # if len(min_heap) > 10:
                #     heapq.heappop(min_heap)
        
        res = []
        counter = 0
        while min_heap and counter < 10:
            res.append(heapq.heappop(min_heap)[1])
            counter += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
