# webpage-displayer



How to use this program:

A user must manually run this program in a terminal.
While running, this program continuously opens and scans a text file named 'article.txt' for the string 'run'.
As soon as it reads the string 'run', it then opens a json file named "article.json".
It then takes the contents of that file and converts it into a dictionary object  with the key-value pair
of 'url' : <valid url> . The program assumes that the user has passed a valid url to a webpage as the value.
The program then writes opens up the 'article.txt' file and writes the string 'ok' to it to let the client know
that the program has processed the request for a webpage to open up in a browser. The program then pops up the 
default browser, opens a new tab and navigates to the url that was passed.


