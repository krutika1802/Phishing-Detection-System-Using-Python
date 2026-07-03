from phishing_keywords import phishing_keywords

# Read emails
with open("sample_emails.txt", "r") as file:
    emails = file.readlines()

print("\n===== PHISHING DETECTION RESULTS =====\n")

for email in emails:

    email = email.strip()
    email_lower = email.lower()

    suspicious = False
    matched_keywords = []

    for keyword in phishing_keywords:

        if keyword in email_lower:
            suspicious = True
            matched_keywords.append(keyword)

    if suspicious:

        print("⚠️ PHISHING DETECTED")
        print("Email:", email)
        print("Matched Keywords:", matched_keywords)
        print("-" * 50)

    else:

        print("✅ SAFE EMAIL")
        print("Email:", email)
        print("-" * 50)