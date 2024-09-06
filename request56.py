#here we learn about request module#
import requests
from bs4 import BeautifulSoup
url="https://www.ilovepdf.com/download/9lqbyhkfjzhf4v1g2th29jj7tq3tt8d5x1mw1hsrv7ty0bqk0wr9klk2hhgkptv2xy1y9v7ds89hp407ycscgj1mns6ty6qyb9gp0jnfclhvw14lbps2p1sr0A70bp1wdj29m7yjk2jwc2lmjd3lnxskrn4qm5mzc42d99kkvkvm7ckA0801/36"
r=requests.get(url)
soup=BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all('h2'):
    print(heading.text)




# response=requests.get("https://www.codewithharry.com")
# print(response.text)





# url="https://jsonplaceholder.typicode.com/posts"

# data={
#     'title': "maaz",
#     'body': 'bhai',
#     'userID': 12,
# }

# headers={
#     'Content-type': 'application/json; charset=UTF-8',
# }

# response=requests.post(url, headers=headers, json=data)

# print(response.text)
