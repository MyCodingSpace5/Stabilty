import requests
import urllib.request as ur

imagegen = input("What image you wanna generate? Enter the prompt here")
url = f"https://api.newnative.ai/stable-diffusion?prompt={imagegen}"
response = requests.request("GET", url)
data = response.json()
print(data[imagegen])
