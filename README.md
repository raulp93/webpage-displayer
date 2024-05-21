# webpage-displayer


# OVERVIEW: 

While running, this program continuously opens and scans a text file named 'article.txt' for the string 'run'.
As soon as it reads the string 'run', it opens up and reads the url that is in the 'url.txt' file and copies it to local variable.
The program assumes that the user has passed a valid url to a webpage as the value.
The program then writes opens up the 'article.txt' file and writes the string 'ok' to it to let the client know
that the program has processed the request for a webpage to open up in a browser. The program then pops up the 
default browser, opens a new tab and navigates to the url that was passed.




# Requirements:

 - In order for this program to be functional, it must be in the same directory as the program that is using the microservice.

  - ensure that the file article.txt is present in the directory
  - ensure that the file url.txt is present in the directory

# Requesting service:

A user must manually run this program in a terminal.

A program must write the word 'run' in to the article.txt file. This lets the webpage microservice that a client program is requesting service. 

The program requesting service must also write the URL of the desired webpage to be displayed in another text file called url.txt. 

# Data transfer:

The data that the program accepts is the word 'run' and a 'url'. At the moment, there is no data validation so if the 
url is not valid, it will simply not load in the browser. 

As soon as the program reads the word 'run', it overwrites that with the word 'ok'. This lets the client know that the request was recieved.


After the program opens up and displays the webpage, it writes the word 'success' to the article.txt file. This is to let the client program know that the operation was successful



