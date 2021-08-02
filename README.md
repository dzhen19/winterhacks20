[![GPSLED](https://img.youtube.com/vi/7viVmr5hqOo/0.jpg)](https://www.youtube.com/watch?v=7viVmr5hqOo)


# Inspiration
It’s that time of year again, it’s snowing and there’s reindeers and candy canes all around us, but it feels different. You would love to meet your relatives and spend time with your friends, but can’t because of COVID-19.

So what should you do? Should you sit at home? No. Should you break the rules? No. Don’t worry. GPSled is here for you.

Sledding has been a popular winter time activity since we can remember. You don’t need anybody except for the people in your house to take part in it, and the only hard part is finding a place to sled. Lucky for you, GPSled takes care of that.

We wanted to develop a sporting helper application that not only applies technologies that we were interested to learn more about, but is also relevant in the state of the world today. GPSled achieves both of these aims and is heavily inspired by the winter and sporting themes of the Winter Hacklympics.

# What it does
GPSled is a fun version of Google Maps that, given a certain location, can search for all the suitable sledding routes around the neighbourhood. It accomplishes this by first pulling accurate satellite data on the various elevations along the streets of a particular neighbourhood, and then calculating slopes for each viable route. It does all this in a seamless fashion allowing the user to have a swift and pleasurable experience. Additionally, It gives the users the ability to preview an image of the preferred sledding location along with other useful information about the street.

# How we built it
For the front-end, we decided to use Facebook’s React framework for its visual appeal and ease of use. We were able to integrate React with MapBox, an open-source mapping platform, flawlessly. Overall we designed a clean and minimal layout that is attractive and filters out important details for the user while hiding the complex mechanism that allows it to work.

The front-end also incorporates several useful Google Maps integrations including Street-View API integration, for generating accurate neighborhood images; Auto-Complete API, for a responsive search bar; and Directions API, for generating route information. Furthermore, it makes use of Material-UI to deliver, and highly-responsive app that is great to look at and easy to work with.

We chose to use Python for the back-end because we found the language simple and the community very supportive. Our team was able to tackle some of the hardest technical problems using Python’s incredible array of libraries. Not only were we successful in integrating various Google Cloud APIs -- Geocoding API, Roads API, and Elevation API -- using their python clients, we also found support for Overpass API that allowed us to query for nodes inside a certain area. The code was easy to debug making rapid development and testing possible.

We used Google Cloud’s Geocoding API to reverse location coordinates and attain their respective street names. This information was useful for the user to make important decisions when selecting routes. The Roads API, an API that returns the nearest road for a certain location coordinate, and Elevation API-- that, given a location coordinate, returns the corresponding elevation--helped calculate slopes for the various routes we were looking at in a given neighborhood. We were able to make accurate slope estimates for different segments of roads and return start and endpoints for eligible routes.

On top of the various APIs, we were also able to make complex algorithmic calculations for determining viable routes using the Haversine module as well as the math library. This made for a perfect runtime allowing us to get swift responses from the back-end server.

After making appropriate implementations, we then used Flask's ability to route to a static frontend file to connect the React App with Flask. Heroku, a platform for deploying applications has good support for Flask so we chose that to deploy our product and make it accessible on the fly.

# Challenges we ran into
As we developed GPSled, we ran into some challenges along the way. Here’s the biggest ones and a bit of detail on each:

Hard time integrating mapbox
Our frontend runs on a combination of Flask and React. Integrating mapbox with this frontend was a difficult task since there were many latitude, longitude connections to be made.
Optimising requests
When we initially created our backend scripts in Python, we were making a large number of calls to the different Google and OverPass APIs. There were two issues with this. Firstly, it increased cost if the project was scaled up, and it increased load time due to latency for each API call. When we tested out our scripts, we realized this and set out to optimise our code. Using Json objects and bundled API calls, we were able to drastically reduce the number of API calls for the two APIs with the highest number of calls, Google Maps Roads API and Google Maps Elevation API.
Manipulating Haversine formula
Even before we built the Python scripts, we knew that there would be a lot of API calls if we couldn’t do distance calculations locally using latitude and longitude coordinates. Hence, we set out to find a way to solve this problem. After some searching we were able to implement the haversine formula to solve this issue. This was just using a library. However, later on we needed to manipulate the haversine formula to move a coordinate based on x metres in any direction. To do this, we manipulated the haversine formula as a function in our python script. This was an especially challenging task.
Using API keys on GitHub
During initial development, we were focussed on coding and kept our GitHub repository private. When we were ready to start deploying the models, we made it public. This caused some issues because our unique API keys became public to anyone looking at the repository. To overcome this challenge, we learnt a new skill: how to use hidden config files to store sensitive data like API Keys. This was a big takeaway for all team members because it is definitely something we will apply in future projects.
Tackling the gaps in Google API
We started the project with a focus on Google’s APIs, however, found that they were unable to fulfill one specific case: finding nodes and their relationships to each other within a given area. To fulfill this, we used the OverPass API on the OverPy Python library. Calls to this API gave us lists of nodes that were on the same road for a given area (a given box). However, these nodes were often just a bit inaccurate, i.e. a little bit off from the road. To correct this, we had to take all these nodes and parse them back to Google’s Road API which would snap the nodes to the nearest road segment. Combining Google’s Road API and OverPass API was a good learning experience for the team. We learnt how APIs can complement each other.
Accomplishments that we're proud of
Throughout the course of our projects there have been numerous personal achievements that we have been proud of. A lot of them are scattered around this page outside of this prompt. Here are some of the major ones:

Finding an API like Overpass that was able to give us relationships between nodes. It’s documentation wasn’t clear on this
Combining multiple APIs to make up for each other’s deficiencies (complement each other)
Creating a back end is able to provide good routes to sled based on the coordinates of the individual’s location
Manipulating haversine’s formula
Learning tonnes of new technologies (More on this below!)
What we learned
Derrick:

Learning how to use google auto-complete
Learning how to deploy Mapbox
Learning how to use Material-UI
Learning how to reverse Geocode using Google APIs
Learning how to connect Flask with React
Rodas:

Working with Material-UI
Working with Flask and React
Working with Google API through direct request as well as through py-pi googlemaps.
Learned how to use LiveShare on VSCode
Learned how to work with Code Sandbox for rapid prototyping
Learned how to effectively work with peers under time constraints.
Sarthak:

Learning all the new Google APIs
Learning how to integrate front-end and back-end using Flask
Learning how to use Linux + Vim as a development environment
Safe usage of Google API keys without exposing them to other users on GitHub
Learning the usefulness of optimising codes in terms of number of API requests. As a result, learnt how to bundle requests to Google APIs
What's next for GPSled
GPSled is ready to hit the shelves. We expect a spike in sledding in the coming season and we hope we hope users enjoy sledding using this app half as much as we enjoyed making it for them. That being said, we hope to add several more features to make the user’s experience more fluid. Here are some of the features:

A social feature where you can invite others to sled with you (for implementation after Covid-19 is over)
A search feature that estimates how many calories you are likely to burn using a certain sledding route
A social feature that checks friends’ sledding activities in realtime
Regional and Global Sledding Challenge where users track their miles to win tournament prizes
Further optimisation of API requests to reduce latency
# Built With
flask
google-cloud
google-elevation
google-roads
haversine
mapbox
material-ui
overpy
pypi-googlemaps
react
