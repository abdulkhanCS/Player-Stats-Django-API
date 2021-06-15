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
