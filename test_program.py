import time

url = "https://en.wikipedia.org/wiki/Rock_paper_scissors"

with open('url.txt', 'w') as outfile:
    outfile.write(url)

with open('article.txt', 'w') as outfile:
    outfile.write('run')

time.sleep(2)

with open('article.txt', 'r') as infile:
    temp = infile.read()



if temp == 'ok':
    print("\nrequest was recieved")
else:
    print("\nthere was a problem with the request")

time.sleep(3)

with open('article.txt', 'r') as infile:
    temp = infile.read()

if temp == 'success':
    print("the webpage was successfully loaded.")

