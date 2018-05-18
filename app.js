
// Require the express engine.
const express = require('express');
const bodyParser = require("body-parser");

const fs = require('fs');
const validate = require('jsonschema').validate;

const path = require('path');

// Create an express application object.
const app = express();
app.use(bodyParser.text({ type: () => 'text' }))

const store = {}

const get_json = (request, response) => {
    const identifier = request.params["identifier"];
    response.send(store[identifier]);
    }

const post_json = (request, response) => {
    let new_profile = request.body
    new_profile = JSON.parse(new_profile)
    // if typeof new_profile is string throw error
    if(typeof new_profile === "string") {
        throw new Error("Service does not handle raw strings.")
    }
    const identifier = request.params["identifier"]
    store[identifier] = new_profile
};

const test_handler = (request, response) => {

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

const post_authenticate = (request, response) => {
    response.send({
        "authenticated": true
    });
};

const get_save = (request, response) => {
    const identifier = request.params["identifier"];
    fs.writeFile(
        identifier + ".json",
        JSON.stringify(store)
    )
}
//make load handler
const get_load = (request, response) => {
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

// Register all of the API listeners.
app.get('/irs/form-k1/2017/ledger', (request, response) => {
    response.send("You got it!")
})

// fs handler for all JSON in data file
const load_json = (request, response) => {
    const foldername = request.params["foldername"];
    const username = request.params["username"];
    const json_folder = "data/" + foldername + "/" + username + ".json";

    console.log (json_folder);
    console.log(username);
    fs.readFile(
        json_folder,
        "utf8",
        (err, data) => {
            if (err) {
                throw err;
            }
            response.send(data);
        }
    )
}
//fs handler for all JSON schemas
const load_schema = (request, response) => {
    const schema = request.params["schema"];
    const json_folder = "schema/" + schema + ".schema.json";

    console.log (json_folder);
    console.log(schema);
    fs.readFile(
        json_folder,
        "utf8",
        (err, data) => {
            if (err) {
                throw err;
            }
            response.send(data);
        }
    )
}


app.post('/user/:username', (request, response) => {
    const username = request.params["username"];
    const user_data = JSON.parse(request.body);

    fs.writeFile(
        "data/user/" + username + ".json",
        JSON.stringify(user_data)
    )

    console.log(user_data);
})




app.post('/accounts/loans/loan0', (request, response) => {
    response.send("Thank you.")
})

app.post('/accounts/loans/loan1', (request, response) => {
    response.send("Thank you.")
})

app.post('/accounts/common-stock/transactions/', (request, response) => {
    response.send("Thank you.")
})

app.post('/accounts/student-loans/transactions/', (request, response) => {
    response.send("Thank you.")
})



app.get('/json/:identifier', get_json);
app.post('/json/:identifier', post_json);
app.post('/test', test_handler);
app.post('/authenticate', post_authenticate);
app.get('/save/:identifier', get_save);
app.get('/load/:identifier', get_load);
app.use('/',express.static(path.join(__dirname, 'static')));
app.get('/data/:foldername/:username', load_json);
app.get('/schema/:schema', load_schema);



port_number = 8888

app.listen(port_number, () =>
    console.log ('app listening on port ' + port_number)

)
