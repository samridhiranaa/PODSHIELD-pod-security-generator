def generate_advice(pods):

    advice_list = []

    for pod in pods:

        pod_name = pod["pod_name"]

        # Root user risk
        if pod["run_as_user"] is None:

            advice_list.append({
                "pod": pod_name,
                "risk": "Container may be running as root",
                "explanation": "Running containers as root increases the impact of container escape vulnerabilities.",
                "recommendation": [
                    "runAsUser: 1000",
                    "allowPrivilegeEscalation: false",
                    "readOnlyRootFilesystem: true"
                ]
            })

        # Privileged container risk
        if pod["privileged"]:

            advice_list.append({
                "pod": pod_name,
                "risk": "Container running in privileged mode",
                "explanation": "Privileged containers gain access to host devices and kernel features, increasing attack surface.",
                "recommendation": [
                    "Remove privileged: true",
                    "Use securityContext with restricted capabilities"
                ]
            })

    return advice_list