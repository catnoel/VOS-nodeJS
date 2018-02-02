const express = require('express');
const app = express();

const store = {
    "name": "cat",
    "location": "boston",
    "job": "developer"
}
app.get('/hello/', (request, response) => 
    {const data = request.params;
    response.send(store)
    }
)

app.listen(8081, () => 
    console.log ('app listening on port 8081')

)