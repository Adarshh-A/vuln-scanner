def calculate_risk(findings):
    score = 0

    for f in findings:
        if f["severity"] == "HIGH":
            score += 3
        elif f["severity"] == "MEDIUM":
            score += 2
        else:
            score += 1

    if score >= 6:
        return "CRITICAL"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"
