# hws-explorer
Product searcher to help people find deals instead of having to filter out using reddit's search problem. This project is grown out of a personal passion to find the best deals for people looking to reuse hardware, and save a chunk of change :-)

 

# Issues:





### Front End Stack
Typescript (imposes types onto the language in order to reduce possible errors)
React (library)
Redux (state management library)
CSS (needs a Sass)
Sass (pre processory, scripting lang that is interpreted or compiled into standard css)
Post-css 
Tailwind (pre designed utility classes to style html elements, compose designs directly in html)
webpack (module bundler)


# API
Can use Graph QL to build and API to communicate between the front end and the back end
Stripe for payment


### Back End Stack
MySQL (relational database, strict but allows for mapping to happen vs non relational database which is easy to use)
Redis (caching database, based on memory, which is much faster)
node js
nest js (handles server side rendering stuff)
type orm allows for this to be done but without having to write raw sql code (Object relational mapper)

### Server
Connects the client side to the database
Connection between client server and db


### Scaling
As your app scales you need to deploy multiple containers so we can use docker + kubernetes, host it on a cloud server, so lets use azure, kubernetes, using terraform instead of manually configuring it (infrastructure as code)

# Notes
Server side = backend stuff



references used to learn how to build this project:

Collecting Data: API vs webscraping https://www.reddit.com/r/TheoryOfReddit/wiki/collecting_data/

API heavily scalable, connection already established
webscraping based on how long it can take? we can use redis here as it is a bit shorter



# Why React Redux?
Managing state is easier, can use context and essentially utilize state in different compoenent leaves; avoid unnecessary props being passed in component wise