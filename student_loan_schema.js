STUDENTLOAN_SCHEMA = {
    type: "object",
    properties:{
        "unique_id": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "phone_number": {
            "type": "string",
            "pattern": ".*([0-9]{3}).*([0-9]{3}).*([0-9]{4}).*"
        },
        "email": {"type": "string"},
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
        "DOB": {
            "type": "string",
            "pattern": "(\\[0-9]{2}/[0-9]{2}/[0-9]{4}\\)"
        },
        "SSN": {
            "type": "string",
            "pattern": "(\\[0-9]{3}-[0-9]{2}-[0-9]{4}\\)"
        },
        "loan_name": {"type": "string"},
        "loan_status": {"type": "string"},
        "account_number": {"type": "string"},
        "school": {"type": "string"},
        "loan_current_balance": {"type": "number"},
        "interest_rate": {"type": "number"},
        "due_date": {
                "type": "string",
                "pattern": "(\\[0-9]{2}/[0-9]{2}/[0-9]{4}\\)"
        },
        "total_current_balance": {"type": "number"}
    }
}

module.exports = STUDENTLOAN_SCHEMA;