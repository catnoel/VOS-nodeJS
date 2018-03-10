OFFERSCHEMA = {
    "student_first_name" : {"type" : "string"},
    "student_last_name" : {"type": "string"},
    "phone_number": {
        "type": "string",
        "pattern": ".*([0-9]{3}).*([0-9]{3}).*([0-9]{4}).*"
    },
    "email": {"type": "string"},
    "school": {"type" : "string"},
    "interest_rate" : {"type" : "string"},
    "interest_accrued" : {"type" : "string"},
    "amount_of_current_loan" : {"type" : "string"},
    "date_borrowed": {
        "type": "string",
        "pattern": "(\\[0-9]{2}/[0-9]{2}/[0-9]{4}\\)"
    },
    "loan_repayment_date": {
        "type": "string",
        "pattern": "(\\[0-9]{2}/[0-9]{2}/[0-9]{4}\\)"
    },
    "bank_loan_servicer" : {"type" : "string"},
    "bank_point_of_contact" : {"type" : "string"},
    "bank_phone_number": {
        "type": "string",
        "pattern": ".*([0-9]{3}).*([0-9]{3}).*([0-9]{4}).*"
    },
    "bank_mailing_address" : {
        "street_address": "string",
        "city": "string",
        "state": "string",
        "zip_code": {
            "type": "string",
            "pattern": "([0-9] {5})"
        },
        "type": "business"
    },
    "documents_attached" : {"type": "string"}
}

module.exports = OFFERSCHEMA;