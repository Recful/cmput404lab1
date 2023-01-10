import requests

print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/Recful/cmput404labs/main/version.py"))