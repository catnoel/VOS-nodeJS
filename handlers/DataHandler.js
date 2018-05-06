
const read_schemas = require("/utilities/read_schemas.js")
const jsonpatch = require("fast-json-patch")


class DataHandler {

  DATA_CACHE = {}

  constructor({ root }) {
    this.root = root

  }

  get({ params: parameters }, { send }) {
    const data_path = parameters['identifier'].split("/")
    let name = data_path.pop()

    let cursor = DATA_CACHE
    for (index of data_path) {
      if (!(index in cursor)) {
        throw 404
      }
      cursor = cursor[index]
    }
    if (name in cursor) {
      send(JSON.stringify(cursor[name]))
    }
  }

  put({ body, params: parameters }) {
    const json = JSON.parse(body)
    if(typeof json == "string") {
      throw new Error("No raw strings")
    }

    const data_path = parameters['identifier'].split("/")
    let name = data_path.pop()

    let cursor = DATA_CACHE
    for (index of data_path) {
      if (!(index in cursor)) {
        cursor[index] = {}
      }
      cursor = cursor[index]
    }
    if (name in cursor) {
      throw new Error(`${parameters['identifier']} is already populated.`)
    }
    cursor[name] = json
  }

  post({ body, params: parameters }, { send }) {
    const json = JSON.parse(body)
    if(typeof json == "string") {
      throw new Error("No raw strings")
    }
    let cursor = DATA_CACHE
    const data_path = parameters['identifier'].split("/")
    let name = data_path.pop()
    for (index of data_path) {
      if (!(index in cursor)) {
        cursor[index] = {}
      }
      cursor = cursor[index]
    }
    if (name in cursor) {
      let index = 0
      while ((name + index) in cursor) {
        index += 1
      }
      name += index
    }
    cursor[name] = json
    send(data_path.concat([name]).join('/'))
  }

  patch({ body, params: parameters }) {
    const patch = JSON.parse(body)
    let cursor = DATA_CACHE
    const data_path = parameters['identifier'].split("/")
    let name = data_path.pop()
    for (index of data_path) {
      if (!(index in cursor)) {
        throw 404
      }
      cursor = cursor[index]
    }
    if (!(name in cursor)) {
      throw 404
    }
    const value = cursor[name]
    const error = jsonpatch.validate(patch, value)
    if (error) {
      throw error.message
    }
    cursor[name] = patch.reduce(jsonpatch.applyReducer, value)
  }

  delete(request, response) {

  }


}

