const http = require('http');

const store = {
    "name": "cat",
    "location": "boston",
    "job": "developer"
}

const app = http.createServer((request, response) => 
    response.end(store)
)

app.listen(8081);

console.log('server running on port 8081');