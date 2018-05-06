
const fs = require('fs');

const read_json = (path, callback) => {
    fs.readFile(
        path,
        "utf8",
        (err, data) => {
            if (err) {
                throw err;
            }
            callback(JSON.parse(data), path)
        }
    )


}

module.export = read_json