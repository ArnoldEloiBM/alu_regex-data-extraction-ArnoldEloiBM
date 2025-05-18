import re

def extract_emails(text):
    """Extracts email addresses, handling malformed and empty input."""
    if not text:
        return []
    try:
        email_form = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(email_form, text)
    except Exception as e:
        print(f"[ERROR] Email extraction failed: {e}")
        return []

def extract_phone_numbers(text):
    """Extracts phone numbers in multiple formats, handles bad input."""
    if not text:
        return []
    try:
        phone_form = r'\(\d{3}\)\s?\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4}|\d{3} \d{3}-\d{4}'
        return re.findall(phone_form, text)
    except Exception as e:
        print(f"[ERROR] Phone number extraction failed: {e}")
        return []

def extract_urls(text):
    """Extracts http/https URLs and handles malformed strings."""
    if not text:
        return []
    try:
        url_form = r'https?://[a-zA-Z0-9./_-]+'
        return re.findall(url_form, text)
    except Exception as e:
        print(f"[ERROR] URL extraction failed: {e}")
        return []

def extract_time(text):
    """Extracts time in 12-hour and 24-hour formats, guards against malformed input."""
    if not text:
        return []
    try:
        time_form = r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?:\s?(?:AM|PM))?\b'
        return re.findall(time_form, text)
    except Exception as e:
        print(f"[ERROR] Time extraction failed: {e}")
        return []

def extract_creditcard(text):
    """Extracts credit card numbers in '#### #### #### ####' or '####-####-####-####' formats."""
    if not text:
        return []
    try:
        creditcard_form = r'\b\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}\b'
        return re.findall(creditcard_form, text)
    except Exception as e:
        print(f"[ERROR] Credit card extraction failed: {e}")
        return []

def extract_currency(text):
    """Extracts currency like $1,234.56 and $19.99, handles malformed strings."""
    if not text:
        return []
    try:
        currency_form = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        return re.findall(currency_form, text)
    except Exception as e:
        print(f"[ERROR] Currency extraction failed: {e}")
        return []

# Sample test string
test_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
For inquiries, call (123) 456-7890 or 123-456-7890 or 123.456.7890.
Visit our website at https://www.example.com or http://sub.example.org/page.
The price is $1,234.56 and on sale for $19.99!
Meeting times are 14:30 and 2:30 PM.
Credit card: 1234 5678 9012 3456 and 1234-5678-9012-3456
"""

# Run each function safely
emails = extract_emails(test_text)
phones = extract_phone_numbers(test_text)
urls = extract_urls(test_text)
cards = extract_creditcard(test_text)
times = extract_time(test_text)
currencies = extract_currency(test_text)

# Nicely print results
print(" Extracted Data:")
print("\n Emails:")
for e in emails:
    print(" -", e)

print("\n Phone Numbers:")
for p in phones:
    print(" -", p)

print("\n URLs:")
for u in urls:
    print(" -", u)

print("\n Credit Cards:")
for c in cards:
    print(" -", c)

print("\n Times:")
for t in times:
    print(" -", t)

print("\n Currency Amounts:")
for cur in currencies:
    print(" -", cur)
