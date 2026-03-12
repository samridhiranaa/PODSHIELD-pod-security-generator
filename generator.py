import yaml
def generate_policy(image, allow_root, profile):
    security_context = {}
    warnings = []
    score = 10
    if profile == "restricted":
        security_context = {
            "runAsNonRoot": True,
            "readOnlyRootFilesystem": True,
            "allowPrivilegeEscalation": False
        }
    elif profile == "baseline":
        security_context = {
            "runAsNonRoot": True
        }
        score -= 2
        warnings.append("Filesystem may not be read-only")
    elif profile == "privileged":
        security_context = {
            "privileged": True
        }
        score -= 5
        warnings.append("Privileged container access enabled")
    if allow_root:
        security_context["runAsNonRoot"] = False
        score -= 3
        warnings.append("Container allowed to run as root")
    policy = {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
            "name": "secure-pod"
        },
        "spec": {
            "containers": [
                {
                    "name": "app",
                    "image": image,
                    "securityContext": security_context
                }
            ]
        }
    }
    yaml_output = yaml.dump(policy)
    report = f"\nSecurity Score: {score}/10\n"
    if warnings:
        report += "\nWarnings:\n"
        for w in warnings:
            report += f"- {w}\n"
    else:
        report += "\nNo security risks detected.\n"
    return report + "\n" + yaml_output