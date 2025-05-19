import re

def extract_emails(text):
    """Extract addresses from text. (e.g. user@example.com or firstname.lastname@company.co.uk)"""
    valid_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    all_candidates = re.findall(r'\S+@\S+', text)
    valid = re.findall(valid_pattern, text)
    invalid = [e for e in all_candidates if e not in valid]
    return valid, [f"Invalid email: {e}" for e in invalid]

def extract_phone_numbers(text):
    """Extract phone numbers from text. (e.g. (123) 456-7890, 123-456-7890, +1 123 456 7890)"""
    valid_pattern = r'\b(\+?\d{1,2}[\s.-]?)?(\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}\b'
    all_candidates = re.findall(r'\d{3}[\s.-]?\d{2,4}[\s.-]?\d{2,4}', text)
    valid_matches = re.findall(valid_pattern, text)
    valid = ["".join(match) for match in valid_matches]
    invalid = [n for n in all_candidates if n not in valid]
    return valid, [f"Invalid phone: {n}" for n in invalid]

def extract_credit_cards(text):
    """Extract credit card numbers. (e.g. 1234 5678 9012 3456 or 1234-5678-9012-3456)"""
    valid_pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b'
    all_candidates = re.findall(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}', text)
    valid = re.findall(valid_pattern, text)
    invalid = [c for c in all_candidates if c not in valid]
    return valid, [f"Invalid card: {c}" for c in invalid]

def extract_currency(text):
    """Extract currency amounts (e.g. $1,234.56, $20.00)."""
    valid_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:\.\d{2})?'
    valid = re.findall(valid_pattern, text)
    all_candidates = re.findall(r'\$\S+', text)
    invalid = [c for c in all_candidates if c not in valid]
    return valid, [f"Invalid currency: {c}" for c in invalid]

def extract_hashtags(text):
    """Extract hashtags from text."""
    pattern = r'#\w+'
    return re.findall(pattern, text), []

def extract_times(text):
    """Extract time formats (12-hour and 24-hour clock)."""
    valid_pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AaPp][Mm])?\b'
    valid_matches = re.findall(valid_pattern, text)
    valid = [match[0] for match in valid_matches if match[0]]
    all_candidates = re.findall(r'\d{1,2}:\d{2}(?:\s?[APap][Mm])?', text)
    invalid = [t for t in all_candidates if t not in valid]
    return valid, [f"Invalid time: {t}" for t in invalid]
