def calculate_security_score(pods):

    score = 100
    breakdown = []

    for pod in pods:

        # Root container penalty
        if pod["run_as_user"] is None:
            score -= 10
            breakdown.append({
                "pod": pod["pod_name"],
                "issue": "Running as root",
                "penalty": -10
            })

        # Privileged container penalty
        if pod["privileged"]:
            score -= 20
            breakdown.append({
                "pod": pod["pod_name"],
                "issue": "Privileged container",
                "penalty": -20
            })

    # Prevent negative score
    if score < 0:
        score = 0

    return score, breakdown