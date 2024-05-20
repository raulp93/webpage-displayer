import webbrowser
import json
import time

# lets user know that the program is running successfully
print("display_article.py is running...")


# this loop allows the program to continue to open and scan the proper text files for requests for service
while True:
    with open("article.txt", "r") as infile:
        text = infile.read()
    
    if text == 'run':
        with open("article.txt", "w") as outfile:
            outfile.write("ok")

        with open("article.json", 'r') as infile:
            request = json.load(infile)

        url = request["url"]

        webbrowser.open(url)

# this sleep is meant to lessen the strain on the processor so that the program is not opening
# and closing the text file millions of times per seccond
    time.sleep(0.25)