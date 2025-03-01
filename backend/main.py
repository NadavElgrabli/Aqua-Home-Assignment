from fastapi import FastAPI, HTTPException
from backend.data_handler import load_users
from backend.models import User
from backend.validation import is_valid_israeli_id, is_valid_phone, normalize_phone_number

app = FastAPI()

# Load valid users into a dictionary (key = ID)
users = load_users("users.json")

@app.get("/users")
def get_all_users():
    """Return all user names."""
    return {"users": [user.Name for user in users.values()]}

@app.get("/users/{name}")
def get_user_by_name(name: str):
    """Retrieve user by name."""
    for user in users.values():
        if user.Name.lower() == name.lower():
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: User):
    """Add a new user."""
    
    # Validate the ID and Phone Number
    if not is_valid_israeli_id(user.ID):
        raise HTTPException(status_code=400, detail="Invalid Israeli ID")
    
    if not is_valid_phone(user.PhoneNumber):
        raise HTTPException(status_code=400, detail="Invalid Phone Number")
    
    # Normalize the phone number
    normalized_phone = normalize_phone_number(user.PhoneNumber)
    
    # Check if the phone number already exists for another user
    for existing_user in users.values():
        if normalize_phone_number(existing_user.PhoneNumber) == normalized_phone:
            raise HTTPException(status_code=400, detail="Phone number already associated with another user")
    
    # Check if the user ID already exists
    if user.ID in users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    
    # Store the user with the normalized phone number
    users[user.ID] = User(
        ID=user.ID,
        Name=user.Name,
        PhoneNumber=normalized_phone,  # Store the normalized version
        Address=user.Address
    )

    return {"message": "User added successfully", "user": users[user.ID]}

