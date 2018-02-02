const request = require('request');

const dict = {
    fname: "Cat",
    lname: "Noel",
    location: "Boston"
};


function getJSON(url, callback) {
    request({
        url: url,
        json: true
    }, function (error, response, body){
        if (!error && response.statusCode === 200) {
            callback(body);
        }
    });
}

getJSON(dict, function (body){
    console.log('here is it: ', body);
});

