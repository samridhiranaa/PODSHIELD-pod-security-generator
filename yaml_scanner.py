import yaml
def scan_yaml(yaml_content):
    try:
        data = yaml.safe_load(yaml_content)
    except Exception as e:
        return ["Invalid YAML format"], []
    issues = []
    fixes = []
    containers = []
    if "spec" in data and "containers" in data["spec"]:
        containers = data["spec"]["containers"]
    elif "spec" in data and "template" in data["spec"]:
        containers = data["spec"]["template"]["spec"]["containers"]
    for c in containers:
        security = c.get("securityContext", {})
        if not security.get("runAsNonRoot", False):
            issues.append("⚠ Container may be running as root")
            fixes.append("runAsNonRoot: true")
        if security.get("privileged", False):
            issues.append("⚠ Container running in privileged mode")
            fixes.append("privileged: false")
        if not security.get("readOnlyRootFilesystem", False):
            issues.append("⚠ Root filesystem is writable")
            fixes.append("readOnlyRootFilesystem: true")
    if not issues:
        issues.append("✔ No major security issues detected")
    return issues, fixes