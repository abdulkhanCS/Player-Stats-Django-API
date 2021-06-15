# Fastbreak API - an API for retrieving NBA player statistics

### To use API, make a GET request to [http://fastbreak-api.herokuapp.com](http://fastbreak-api.herokuapp.com) (API calls might take several seconds at first if link is [asleep](https://devcenter.heroku.com/articles/dynos#dyno-sleeping))

##### Note that only data from 1984-2021 is supported at the moment.

GET requests should adhere to the following schema:

![Request template](https://i.imgur.com/Z1zPAJr.png)


##### Note that if the requested season is 2020-2021, the latter year (2021 in this case) should be entered. Alternatively 2020-2021 can also be entered for the season field. 

## Making a Request

The following code makes a request to FastbreakAPI and retrieves player data using Axios. To use Axios, install the client through typing the command ```npm install axios``` in your current working directory. The code below can be found under the demo folder in demo.js. 

![Working example](https://i.imgur.com/7jYnIUF.png)

The output of the ```console.log()``` statement in line 19 results in the following output:

![Working example JSON payload](https://i.imgur.com/pwf5bBK.png)
Where any field of the json payload can be accessed through ```data['<field']```.

## Error Cases

If the name of the requested player is spelled incorrectly or otherwise unrecognized:

![Error example 1](https://i.imgur.com/6SlXQg1.png)

The JSON payload will be retrieved with a status 400 and errorCode 01:

![Error example 1](https://i.imgur.com/AzSoOMz.png)

If the requested date is a day where the requested player did not play in a game:

![Error example 1](https://i.imgur.com/1AKAqDq.png)

The JSON payload will be retrieved with a status 400 and errorCode 02:

![Error example 1](https://i.imgur.com/IwFAww5.png)
