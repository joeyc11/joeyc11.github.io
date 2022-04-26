import tweepy

auth = tweepy.OAuthHandler("HcH4WfrpF5Mgckr1NhoWfaFRP","oLG0HlARiuYuomFa4hunZZrKxapHxffuUhmtAIiUCJpGAYuZ0O")
auth.set_access_token("4845021440-UZdgVWF1zy3j0vfDZJWQf2RFtCPuDEOFq4LNAoB","Xx7x8wlSxMLFZdhXLa4Goe2QuDGMAnAO9oobKRHX74VH2")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("authentication ok")
except:
    print("fail")
    