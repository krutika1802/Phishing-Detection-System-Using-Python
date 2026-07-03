import re
from phishing_keywords import phishing_keywords


def extract_urls(text):

    return re.findall(r'https?://\S+', text)


with open("sample_emails.txt") as file:
    emails = file.readlines()


for email in emails:

    email = email.strip()
    score = 0

    matched_keywords = []

    for keyword in phishing_keywords:

        if keyword in email.lower():
            score += 1
            matched_keywords.append(keyword)

    urls = extract_urls(email)

    if urls:
        score += 2

    if score >= 2:

        print("\n⚠️ PHISHING EMAIL")
        print(email)
        print("Keywords:", matched_keywords)
        print("URLs:", urls)

    else:

        print("\n✅ SAFE EMAIL")
        print(email)