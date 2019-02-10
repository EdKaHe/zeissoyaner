import requests

test = requests.get("https://hackathonblobmunich.blob.core.windows.net/data/meta.csv?sv=2018-03-28&ss=bf&srt=sco&sp=rwdlac&se=2019-02-10T00:11:41Z&st=2019-02-09T16:11:41Z&spr=https&sig=990snkpPPqWbTtbdKTC%2B9%2FpowSOUa%2FWSbBNkY5fHoEI%3D").text

print(test)