# Fastbreak API - an API for retrieving NBA player statistics

### To use API, make a GET request to [http://fastbreak-api.herokuapp.com](http://fastbreak-api.herokuapp.com) (API calls might take several seconds at first if link is [asleep](https://devcenter.heroku.com/articles/dynos#dyno-sleeping))

Note that only data from 1984-2021 is supported at this moment.

GET requests should adhere to the following schema:

![Request template](https://i.imgur.com/Z1zPAJr.png)


Note that if the requested season is 2020-2021, the latter year (2021 in this case) should be entered. Alternatively 2020-2021 can also be entered for the season field. 

## Example

Given the following GET request:

![Working example](https://i.imgur.com/ogN1fhl.png)

The following JSON payload would be retrieved: 

![Working example JSON payload](https://i.imgur.com/uHLnTxU.png)

## Error Cases

If the name of the requested player is spelled incorrectly or otherwise unrecognized:

![Error example 1](https://i.imgur.com/6SlXQg1.png)

The JSON payload will be retrieved with a status 400 and errorCode 01:

![Error example 1](https://i.imgur.com/AzSoOMz.png)

If the requested date is a day where the requested player did not play in a game:

![Error example 1](https://i.imgur.com/1AKAqDq.png)

The JSON payload will be retrieved with a status 400 and errorCode 02:

![Error example 1](https://i.imgur.com/IwFAww5.png)

