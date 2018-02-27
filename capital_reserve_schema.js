capitalreserve_schema = {
    type: "object",
    propperties: {
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "phone_number": {
            "type": "string",
            "pattern": ".*([0-9]{3}).*([0-9]{3}).*([0-9]{4}).*"
        },
        "email": {"type": "string"},
        "username": {"type": "string"},
        "mailing_address": {
            "street_address": "string",
            "city": "string",
            "state": "string",
            "zip_code": {
                "type": "string",
                "pattern": "([0-9] {5})"
            },
            "type": "business"
        },
        "tax_identification_number": {
            "type": "string",
            "pattern": "([0-9]{2}).*([0-9]{7})"
        },
        "amount_contributed": {"type": "number"},
        "date": {
            "type": "string",
            "pattern": "(\\[0-9]{2}/[0-9]{2}/[0-9]{4}\\)"
        }

    },
    required: ["first_name", "mailing_address"]
}

module.exports = capitalreserve_schema;