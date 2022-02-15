# project1-rfair3

Link to Heroku: https://calm-thicket-01978.herokuapp.com/

For anyone looking to clone my repository and run the app locally:
You will need to install Flask, requests, dotenv, and the Wikipedia-api. 
You will also need to register for an api key from The Movie Database. 
The API key that you will need is version 3 and make sure to export the key in an .env file as such:

export api_key= “YOUR API KEY HERE”

Make sure to also add the .env file to a .gitignore file.
This is all of the requirements to get the app up and running locally. 



I have one problem that is not fixed. For the genre titles, the genre id prints with the genre title.
For the app, I do not want any of the genre ids to show that come from The Movie Database. 
To address this, I would like to do more research on how to extract the name from the id. 
I tried filtering out the numbers using isdigit() but, this was unsuccessful. 
I would love to add the option to choose a movie from a list then the page loads up with the title tagline poster and Wiki page.



2 technical issues that arose during the building process was trying to pull the results from The Movie Database and getting the app to run on refresh in browser. 
For the first technical issue, I was trying to use json to call results from TMDB.
The URL that I was using does not have a results call. 
With that being said, I ended up calling each title separately using parse. 
I used a YouTube video as well as various forums from stack overflow. 
For the second issue, to get another movie to appear on the website, I had to stop running app.py and rerun the app.py code. 
To fix this issue I watched the lectures as well as looked up how to run a dynamic website in python. 
Stacked overflow helped tremendously.


Right before submission, I accidentally merged 2 folders together on GitHub which resulted in me deleting my original repository.
In the original repository, I had 11 commits in total but with the new repository, I have nowhere near the same amounts of commits. 
