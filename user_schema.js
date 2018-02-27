USER_SCHEMA = {
        type: "object",
        properties: {
            "first_name": { "type": "string" },
            "last_name": { "type": "string" },
            "phone_number": { 
                "type": "string",
                "pattern": ".*([0-9]{3}).*([0-9]{3}).*([0-9]{4}).*",

            },
            "email": { "type": "string" },
            "username": { "type": "string" }
        },
        required: ["email", "username", "phone_number"]
    }

module.exports = USER_SCHEMA;