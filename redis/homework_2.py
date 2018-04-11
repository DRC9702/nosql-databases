import redis
import datetime


ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

def article_vote(redis, user, article):
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)

    if not datetime.datetime.fromtimestamp(redis.zscore('time:', article)) < cutoff:
        article_id = article.split(':')[-1]
        if redis.sadd('voted:' + article_id, user):
            redis.zincrby(name='score:', value=article, amount=VOTE_SCORE)
            redis.hincrby(name=article, key='votes', amount=1)

def article_switch_vote(redis, user, from_article, to_article):
    # HOMEWORK 2 Part I
    cutoff = datetime.datetime.now() - datetime.timedelta(seconds=ONE_WEEK_IN_SECONDS)

    # Check that the articles can both be voted on
    from_time = datetime.datetime.fromtimestamp(redis.zscore('time:', from_article))
    to_time = datetime.datetime.fromtimestamp(redis.zscore('time:', to_article))

    if not from_time < cutoff and not to_time < cutoff:
        from_id = from_article.split(':')[-1]
        to_id = from_article.split(':')[-1]
        # Check that can move user from 'from' to 'to'
        if redis.smove('voted:'+ from_id, 'voted:'+to_id, user):
            redis.zincrby(name='score:', value=from_article, amount=-1*VOTE_SCORE)
            redis.hincrby(name=from_article, key='votes', amount=-1)
            redis.zincrby(name='score:', value=to_article, amount=VOTE_SCORE)
            redis.hincrby(name=to_article, key='votes', amount=1)

redis = redis.StrictRedis(host='localhost', port=6379, db=0)
# user:3 up votes article:1
article_vote(redis, "user:3", "article:1")
# user:3 up votes article:3
article_vote(redis, "user:3", "article:3")
# user:2 switches their vote from article:8 to article:1
article_switch_vote(redis, "user:2", "article:8", "article:1")

# Which article's score is between 10 and 20?
# PRINT THE ARTICLE'S LINK TO STDOUT:
# HOMEWORK 2 Part II
article = redis.zrangebyscore('score:','10','20')
print redis.hget(name=article[0],key='link')

