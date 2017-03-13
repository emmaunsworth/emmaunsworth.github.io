from flask import Flask
from flask import render_template
from flask import request


app = Flask("MyApp")


def tweepy_bit(hashtag):
    # argfile = str(sys.argv[1])

    # enter the corresponding information from your Twitter application:
    CONSUMER_KEY = 'R3Tq8gxuUv3PgSYxwpBsLQvS7'  # keep the quotes, replace this with your consumer key
    CONSUMER_SECRET = 'TL8sio0UN3E6DqTDem1E5co8AWsb5CU1DXdazJ32A2s2JTwzu7'  # keep the quotes, replace this with your consumer secret key
    ACCESS_KEY = '828674028344840192-yrTlABlmNDp9ejhSelGyLEZ5LKggevi'  # keep the quotes, replace this with your access token
    ACCESS_SECRET = 'CZABgzlzkK4sSFaJgOLmik1qyQ5kViTjDPOcy8rc6O02a'  # keep the quotes, replace this with your access token secret
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    nastywomen_tweets = api.search(
        q=hashtag
    )

    for tweet in nastywomen_tweets:
        print tweet.user.name + ": " + tweet.text


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/gettweet")
def hello_someone(name):
    return render_template("hello.html", name=name.title())


@app.route("/gettweet", methods=['POST'])
def sign_up():
    form_data = request.form
    print form_data['name']
    print form_data['email']
    tweepy_bit()
    return "ALL OK"

app.run()
