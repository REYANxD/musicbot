HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["7671835"])
    API_HASH = environ["66eb32d104cfee53abe66e2b59eb06f7"]
    SESSION_STRING = environ[
        "AQAqVlcVeHAmWuRhuNbk75sxbjzSOWus8VHiIB7TP228uWpG3yt0UIPE-J0l8wJHLjNC7IxdhbDDPlWaS76WdDRIN_lC1zJ1oFiRIpq_TCgXyYDeAfpEMeXjXO3oTTfiYWvqcsTiaVyDg_zBGg5lmX4UhZy-3cHjZN6AfeQqD4oNUl-6ODnmwgXKNqUQiFpLw-WHt-PYqsZDDA0YXC9tmzDr3A9cuZkk6tjzRTN5yJvC2U5qnTgiZ3ROy5e_h8ol4Ne6P89RJwjKRVDgsA1B-BtLy0-Lmg2Xdgy4e7pAajByuDdX23dIyeZVjM5hM-OkX9ggqOAM_5KQ0rkN7EQWqMyRdq5WJAA"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["WZWELK-DUXWSB-KWBHCC-ACJOQZ-ARQ"]
    CHAT_ID = int(environ["-1001559362375"])
    DEFAULT_SERVICE = environ.get("youtube") or "youtube"
    BITRATE = int(environ["512"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 7671835
    API_HASH = "66eb32d104cfee53abe66e2b59eb06f7"
    ARQ_API_KEY = "WZWELK-DUXWSB-KWBHCC-ACJOQZ-ARQ"
    CHAT_ID = -1001559362375
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320
    SESSION_STRING = "AQAqVlcVeHAmWuRhuNbk75sxbjzSOWus8VHiIB7TP228uWpG3yt0UIPE-J0l8wJHLjNC7IxdhbDDPlWaS76WdDRIN_lC1zJ1oFiRIpq_TCgXyYDeAfpEMeXjXO3oTTfiYWvqcsTiaVyDg_zBGg5lmX4UhZy-3cHjZN6AfeQqD4oNUl-6ODnmwgXKNqUQiFpLw-WHt-PYqsZDDA0YXC9tmzDr3A9cuZkk6tjzRTN5yJvC2U5qnTgiZ3ROy5e_h8ol4Ne6P89RJwjKRVDgsA1B-BtLy0-Lmg2Xdgy4e7pAajByuDdX23dIyeZVjM5hM-OkX9ggqOAM_5KQ0rkN7EQWqMyRdq5WJAA"

# don't make changes below this line
ARQ_API = "https://thearq.tech"
