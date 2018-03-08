const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require("body-parser");
const validate = require('jsonschema').validate;
const capitalreserve_schema = require('./capital_reserve_schema.js');
const USER_SCHEMA = require('./USER_SCHEMA.js');
const STUDENTLOAN_SCHEMA = require('./student_loan_schema.js');
const REPAYMENT_SCHEMA = require('./repayment_schema.js');


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

const all_post_handler = (request, response) => {

    const request_body_json = JSON.parse(request.body);

    console.log(validate(request_body_json, USER_SCHEMA, { throwError: true }));
    
    const new_user = request_body_json;
    
    console.log("Thank you " + new_user["first_name"] + "! " + 
    "You have created username: " + new_user["username"] + 
    " and email: " + new_user["email"] + " for your login credentials.");

    const identifier = request.params["identifier"];
    store[identifier] = new_user;
    response.send(store[identifier]);
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

app.get('/json/:identifier', get_handler);
//app.post('/json/:identifier', post_handler);
//app.get('/front_page', my_webpage);
//app.post('/test', all_post_handler);
app.use('/',express.static(path.join(__dirname, 'static')));





app.listen(8081, () => 
    console.log ('app listening on port 8081')

)
