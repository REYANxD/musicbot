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
    API_ID = 7475191
    API_HASH = "32dbc9e8368cca754844f77399f6db81"
    ARQ_API_KEY = "TNMEAT-LJUCUR-NKKNHA-HSAXCC-ARQ"
    CHAT_ID = -1001517082431
    DEFAULT_SERVICE = "youtube"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320
    SESSION_STRING = "AQCxWYaFJXCpaAozF6OoH0foTNrRpC1pKKO3PWwF51KqkQYW7ZO_UgB5hl3mqi59VV1iyGPpZRbURvCp6VuX0IxpIywRpNsBAATEPLNHd7JCBLBhx3EEu9_rgT2o1p7BXuNAGPv9e3ANEGJwGxfTrog5pg55cPazNgRnBD2bsEbLDOnQ_zm6EXXnJ7pUw1IBySxXql33xUl6mvgh3sfyexQnI10SPKUjikMFkZf3dhhLlTvdapOS4Kqseqn2TYRI8-ajSEjyJDwWTow6h0zVZtYTwkYQDMlDSDgyLs5oQLhabjwR6ryt4rXtjZm9y5giOteD47l-DASpZ7rgtx5k-MAOcu_qiwA"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
