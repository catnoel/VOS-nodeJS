
const read_json = require("utilities/read_json.js")

const what_i_want_to_do = (json) => {
  console.log("hey, I have json!")
  console.log(json)
}

what_i_want_to_do()

read_json("package-lock.json", what_i_want_to_do())