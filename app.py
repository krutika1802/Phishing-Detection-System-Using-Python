# List of phishing keywords
phishing_keywords = [
    "click here",
    "verify",
    "urgent",
    "free",
    "win",
    "password",
    "login",
    "bank account",
    "secure your account"
]

# Read sample emails
with open("sample_emails.txt", "r") as file:
    emails = file.readlines()

print("\n--- Phishing Detection Results ---\n")

# Analyze emails
for email in emails:
    email_lower = email.lower()

    suspicious = False

    for keyword in phishing_keywords:
        if keyword in email_lower:
            suspicious = True
            break

    if suspicious:
        print(f"⚠️ Suspicious Email: {email.strip()}")
    else:
        print(f"✅ Safe Email: {email.strip()}")