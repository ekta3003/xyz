import requests

x = requests.get('https://tsneh.vercel.app/hs9bygr7au91')

with open("3760393314e0a5b393ad60eb24565ecd.m3u", "w") as f:
    f.write(x.text)
