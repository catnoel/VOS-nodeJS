const read_schema = require("read_schema")
const Validator = require('jsonschema').Validator

const read_schemas = (callback) => {
    read_schema("/schema/capital_reserve.schema.json", callback)
    read_schema("/schema/form-k1.schema.json", callback)
    read_schema("/schema/offer.schema.json", callback)
    read_schema("/schema/repayment.schema.json", callback)
    read_schema("/schema/student_loan.schema.json", callback)
    read_schema("/schema/user.schema.json", callback)
}

const load_validator = () => {
    const new_validator = new Validator()
    const ready = new Promise()

    read_schemas((schema, path) => {
        new_validator.addSchema(schema, path)
    })

  return new_validator
}