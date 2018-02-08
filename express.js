const express = require('express');
const app = express();
const bodyParser = require("body-parser");

app.use(bodyParser.text({
    type: function(req) {
        return 'text';
    }
}));

const store = {
    "cat_profile": {
        "name": "cat",
        "location": "boston",
        "job": "developer"
    }
}

const get_handler = (request, response) => {
    const identifier = request.params["identifier"];
    response.send(store[identifier]);
    }

const post_handler = (request, response) => {
    let new_profile = request.body;
    new_profile = JSON.parse(new_profile);
    // if typeof new_profile is string throw error
    if(typeof new_profile === "string") {
        throw new Error("Service does not handle raw strings.")
    }
    const identifier = request.params["identifier"];
    store[identifier] = new_profile;
    console.log(store);
    response.send(store);
};

//static handler
const my_webpage = (request, response) => {
    response.send(`
    <html>
    <head>
    </head>
    <body>
    <p>Hello World!</p>
    <input placeholder="Enter a value">
    </body>
    </html>`)
    };

app.post('/json/:identifier', post_handler);
app.get('/json/:identifier', get_handler);
app.get('/front_page', my_webpage);



app.listen(8081, () => 
    console.log ('app listening on port 8081')

)