// We presume to be able to read a schema.
const read_schema= require("/utilities/read_schema.js")

// We're going to use the Validator class to create a validator.
const json_schema = require("json-schema")

// We're only going to have one validator over the program's lifetime.
const validator = new json_schema.Validator()


class Schema {

  constructor(path) {
    this.path = path
    this.loading = new Promise()
    read_schema(path, (json) => {
      this.json = json
      this.loading.resolve(json, this)
    })
  }

  ready(callback) {
    this.loading.then(callback)
  }



}