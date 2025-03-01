def is_valid_israeli_id(id_number: str) -> bool:
    """Validate Israeli ID (9 digits, checksum)."""
    id_number = id_number.strip()
    
    # Ensure it's a valid 9-digit number
    if not id_number.isdigit() or len(id_number) != 9:
        return False
    
    # Implement the checksum logic
    digits = [int(digit) for digit in id_number]
    checksum = 0
    
    for i, digit in enumerate(digits):
        step = digit * ((i % 2) + 1)
        checksum += step if step <= 9 else step - 9
    
    return checksum % 10 == 0


def is_valid_phone(phone: str) -> bool:
    """Validate Israeli phone number format (e.g., 0541234567 or +972541234567)."""
    phone = phone.strip()  # Remove any leading/trailing spaces

    # Check if the phone starts with "05" and has exactly 10 digits
    if len(phone) == 10 and phone[:2] == "05" and phone[2:].isdigit():
        return True
    
    # Check if the phone starts with "+9725" and has exactly 11 digits
    if len(phone) == 13 and phone[:4] == "+972" and phone[4:5] == "5" and phone[5:].isdigit():
        return True
    
    return False

def normalize_phone_number(phone: str) -> str:
    """Normalize phone number (e.g. from 0541234567 to +972541234567)."""
    phone = phone.strip()
    
    # If the phone number starts with 05, replace it with +9725
    if phone.startswith("05"):
        phone = "+972" + phone[1:]
    
    return phone

