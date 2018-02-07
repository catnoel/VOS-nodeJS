const express = require('express');
const app = express();
const bodyParser = require("body-parser");

const store = {
    "cat_profile": {
        "name": "cat",
        "location": "boston",
        "job": "developer"
    },
    "brian_profile": {
        "name": "brian",
        "location": "boston",
        "job": "developer"
    }
}

// app.get('/json/:identifier', (request, response) => {
//     const identifier = request.params["identifier"];
//     response.send(store[identifier])
//     }
// )

app.use(bodyParser.text({
    type: function(req) {
        return 'text';
    }
}));



const postHandler = (request, response) => {
    const storeBody = request.body;
    const identifier = request.params["identifier"];
    response.send(JSON.stringify(storeBody[identifier]));
    //console.log(results);
    console.log(JSON.stringify(storeBody));
};

const postHandler2 = (request, response) => {
    let newProfile = new Object;
    newProfile = request.body;
    const identifier = request.params["identifier"];
    store.cat_profile[newProfile] = request.body.identifier
    console.log(store);
    response.send(store);
    };

app.post('/json/:identifier', postHandler2);

// app.put('/json/:identifier', (request, response) => {
//     const identifier = request.params["identifier"];
//     const data = request.body;
//     response.send(data);
//     }
// )

app.listen(8081, () => 
    console.log ('app listening on port 8081')

)