import json
from backend.models import User
from backend.validation import is_valid_israeli_id, is_valid_phone, normalize_phone_number

def load_users(filename: str) -> dict:
    """Load users from JSON and validate them."""
    with open(filename, 'r') as file:
        data = json.load(file)

    users = {}
    for user in data:
        # Validate ID
        if not is_valid_israeli_id(user["ID"]):
            print(f"Invalid ID for user {user['Name']}, skipping.")
            continue
        
        # Validate and normalize phone number
        if not is_valid_phone(user["PhoneNumber"]):
            print(f"Invalid phone number for user {user['Name']}, skipping.")
            continue
        
        # Normalize phone number to a consistent format before saving
        user["PhoneNumber"] = normalize_phone_number(user["PhoneNumber"])

        users[user["ID"]] = User(**user)
    
    return users
