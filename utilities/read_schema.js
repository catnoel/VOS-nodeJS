const read_json = require("read_json.js")

const read_schema = (path, callback) => {
  const target_suffix = ".schema.json"
  if (path.slice(-target_suffix.length) === target_suffix) {
    throw `Invalid schema path: ${path} does not end with .schema.json.`
  }
  read_json(path, callback)

}