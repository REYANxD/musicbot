HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ["SESSION_STRING"]  
# Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 8841293
    API_HASH = "77920a25c9bf9cc8c193ca6fe28352e7"
    ARQ_API_KEY = "TNMEAT-LJUCUR-NKKNHA-HSAXCC-ARQ"
    CHAT_ID = -1001517082431
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320
    SESSION_STRING = "AQCLRG7I_Esiqdv2wYylRMPxNKnzfCQEcDIhHmYm9eO9ccmqDrBMecKz6xElXxCZ-cxm3FfyyJ0ABpeQJf9BQttW9yUrtvvyT7b5ApyhJ-ySsqNzqUeTCGUwhHEnGUkgSe-9zzkiK7Tgz_jIkX34nrZ028IGX-Q-Sia6IKWVS8Gfbw1Efs4x1ZZLIK418GVAXZt0DlK2mUnpwiSOceOZxJMrM3KB-Agc768OlBYdaRRLA2mNC5QyF2RE2UXS9sEtKl9ylu8rgGGPbV2zxxV-xyN8zE8kPFSSjnbquxJgcS19o5nxkt-F-BIeI6Q1Hg2BdQgT9V6ncoJqZSmN3y9eXfefeMiwvQA"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
