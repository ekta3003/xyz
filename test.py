import requests

x = requests.get('https://tsneh.vercel.app/hs9bygr7au91')

with open("index.html", "w") as f:
    f.write(x.text)
