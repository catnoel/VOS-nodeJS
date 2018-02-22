const express = require('express');
const app = express();
const bodyParser = require("body-parser");
const validate = require('jsonschema').validate;


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

const userpost_handler = (request, response) => {
    let new_user = request.body;
    new_user = JSON.parse(new_user);
    console.log(validate(new_user, {"type": "object"}));
    
    new_user = {
        first_name: new_user["name"],
        email: new_user["email"],
        username: new_user["username"]
    }
    
    console.log("Thank you " + new_user["first_name"] + "! " + 
    "You have created username: " + new_user["username"] + 
    " and email: " + new_user["email"] + " for your login credentials.");
    const identifier = request.params["identifier"];
    store[identifier] = new_user;
    console.log(store);
    response.send(store);
    
};
// const userpost_handler2 = (request, response) => {

//     let name = request.body.name;
//     let email = request.body.email;
//     let username = request.body.username;
//     let password = request.body.password;
            
//     console.log("you posted: First Name: " + name);
//     response.send(store);
// };

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

app.get('/json/:identifier', get_handler);
//app.post('/json/:identifier', post_handler);
//app.get('/front_page', my_webpage);
app.post('/test', userpost_handler);




app.listen(8081, () => 
    console.log ('app listening on port 8081')

)
