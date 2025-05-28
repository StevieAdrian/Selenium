test_cases = [
    {
        "desc": "Success - Valid StudentID and DOB",
        "student_id": "2702332753",
        "dob": {"year": "2005", "month": "April", "day": "27"},
        "response": True
    },
    {
        "desc": "Fail - Invalid StudentID",
        "student_id": "1234567890",
        "dob": {"year": "2005", "month": "April", "day": "27"},
        "response": False
    },
    {
        "desc": "Fail - Invalid Date of Birth",
        "student_id": "2702332753",
        "dob": {"year": "1919", "month": "February", "day": "13"},
        "response": False
    },
    {
        "desc": "Fail - Both StudentID and DOB are invalid",
        "student_id": "1234567890",
        "dob": {"year": "1919", "month": "February", "day": "13"},
        "response": False
    }
]
