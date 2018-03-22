const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require("body-parser");
const fs = require('fs');
const validate = require('jsonschema').validate;
const capitalreserve_schema = require('./capital_reserve_schema.js');
const USER_SCHEMA = require('./USER_SCHEMA.js');
const STUDENTLOAN_SCHEMA = require('./student_loan_schema.js');
const REPAYMENT_SCHEMA = require('./repayment_schema.js');
const OFFER_SCHEMA = require('./offer_schema.js');


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

const offer_handler = (request, response) => {
    const request_body_json = JSON.parse(request.body);
    console.log(validate(request_body_json, USER_SCHEMA, { throwError: true }));

};

const authenticate_handler = (request, response) => {
    response.send({
        "authenticated": true
    });
};

const savefile_handler = (request, response) => {
    const identifier = request.params["identifier"];
    fs.writeFile(
        identifier + ".json",
        JSON.stringify(store)
    )
}
//make load handler

const loadfile_handler = (request, response) => {
    const identifier = request.params["identifier"];
    fs.readFile(
        "./test.txt",
        "utf8",
        (err,data) => {
            if (err) {
                throw err;
            } 
            console.log(data);
        }
    )
}

app.get('/json/:identifier', get_handler);
app.post('/json/:identifier', post_handler);
app.post('/test', all_post_handler);
//app.use('/',express.static(path.join(__dirname, 'static')));
app.post('/authenticate', authenticate_handler);
app.get('/save/:identifier', savefile_handler);
app.get('/load/:identifier', loadfile_handler);



app.listen(8081, () => 
    console.log ('app listening on port 8081')

)
