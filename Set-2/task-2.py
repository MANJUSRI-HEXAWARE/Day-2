from datetime import date
import re
def normalize_policy(policy_number):
    return "".join(str(policy_number).split()).casefold()
def normalize_date(incident_date):
    if isinstance(incident_date, date):
        return incident_date.isoformat()
    value = re.sub(r"\s+", "", str(incident_date))
    return date.fromisoformat(value).isoformat()
def claim_key(claim):
    return normalize_policy(claim["policy_number"]), normalize_date(claim["incident_date"])
def find_duplicates(claims):
    seen = {}
    duplicates = []
    for claim in claims:
        key = claim_key(claim)
        if key in seen:
            duplicates.append((claim["claim_id"], seen[key]))
        else:
            seen[key] = claim["claim_id"]
    return duplicates
if __name__ == "__main__":
    claims = [
        {"claim_id": "CL001", "policy_number": "POL 123 A", "incident_date": "2026-11-01"},
        {"claim_id": "CL002", "policy_number": "pol123a", "incident_date": " 2026-11-01 "},
        {"claim_id": "CL003", "policy_number": "POL-456", "incident_date": "2026-11-02"},
        {"claim_id": "CL004", "policy_number": " pol - 456 ", "incident_date": "2026-11-02"},
        {"claim_id": "CL005", "policy_number": "POL123A", "incident_date": "2026-11-03"},
    ]
    print("Duplicate (claim, original) pairs:", find_duplicates(claims))
    print("Empty input:", find_duplicates([]))
