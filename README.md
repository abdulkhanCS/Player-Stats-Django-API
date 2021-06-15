# Fastbreak API - an API for retrieving NBA player statistics

### To use API, make a GET request to [http://fastbreak-api.herokuapp.com](http://fastbreak-api.herokuapp.com) (API calls might take several seconds at first if link is [asleep](https://devcenter.heroku.com/articles/dynos#dyno-sleeping))

##### Note that only data from 1984-2021 is supported at the moment.

##### Note that if the requested season is 2020-2021, the latter year (2021 in this case) should be entered. Alternatively 2020-2021 can also be entered for the season field. 

## Making a Request

The following code makes a request to FastbreakAPI and retrieves player data using Axios. To use Axios, install the client through typing the command ```npm install axios``` in your current working directory. The code below can be found under the demo folder in demo.js. 

```
const axios = require('axios')

async function getPlayerData(){
  try { 
    const response = await axios.get('http://fastbreak-api.herokuapp.com', 
      { data: { 
        player: 'Kobe Bryant',
        date: '01/22', 
        season: '2006' 
      } })
      return response
  } catch (error) { console.log(error) }
}

getPlayerData()
  .then(response => response.data)
  .then((data) => {
    if(data["status"] == 200){
      console.log(data)
      //DO SOME WORK WITH DATA
    }
    else{
      console.log("FastbreakAPI returned an error of ", response[status])
    }
  }) 
```

Note that the ```data``` of the GET request should adhere to the following schema:

```
"player" : "First Last", 
"date" : "MM/DD",
"season" : "YYYY"
```



The output of the ```console.log()``` statement in line 19 results in the following output:
```
{
  status: 200,
  statline: {
    points: '81',
    rebounds: '6',
    assists: '2',
    steals: '3',
    blocks: '1',
    turnovers: '3',
    minutes: '42',
    field_goals: '28-46',
    three_pointers: '7-13',
    free_throws: '18-20',
    fg_percentage: '60.9',
    three_point_percentage: '53.8',
    ft_percentage: '90.0',
    personal_fouls: '1'
  },
  date: 'Sun 1/22',
  team_played: 'vsTOR',
  score: 'W122-104'
}
```

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

