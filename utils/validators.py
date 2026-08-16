from exceptions import *   
try:
    def validate_name(name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")

    def validate_email(email):
        if not email.strip():
            raise ValueError("Email cannot be empty.")
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

    def validate_phone(phone):
        if not phone.strip():
            raise ValueError("Phone number cannot be empty.")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be a 10-digit number.")

    def validate_address(address):
        if not address.strip():
            raise ValueError("Address cannot be empty.")

    def validate_account_type(account_type):
        if account_type.lower() not in ["savings", "current"]:
            raise ValueError("Account type must be either 'savings' or 'current'.")

except ValueError as e:
    print(f"Validation error: {e}")