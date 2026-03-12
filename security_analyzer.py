def analyze_security(pods):
    issues = []
    for pod in pods:
        if pod["privileged"]:
            issues.append(f"{pod['pod_name']} is running in privileged mode")
        if pod["run_as_user"] is None:
            issues.append(f"{pod['pod_name']} may be running as root")
    return issues