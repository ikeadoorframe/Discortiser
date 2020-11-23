AdsText = """Ads are chosen at random.
Use a new ad in every line:
ad #1
ad #2
ad #3
If you are using multiple accounts, it's best to have more ads."""

ads = open("../data/AdList.txt", "w")
ads.write(AdsText)
ads.close()
exit()
