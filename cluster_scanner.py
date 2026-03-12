from kubernetes import client, config
def scan_cluster():
    # Load Kubernetes config
    config.load_kube_config()
    v1 = client.CoreV1Api()
    pods = v1.list_pod_for_all_namespaces(watch=False)
    pod_data = []
    # Namespaces to ignore (system components)
    ignored_namespaces = [
        "kube-system",
        "kube-public",
        "kube-node-lease"
    ]
    for pod in pods.items:
        # Skip system namespaces
        if pod.metadata.namespace in ignored_namespaces:
            continue
        for container in pod.spec.containers:
            security = container.security_context
            pod_data.append({
                "pod_name": pod.metadata.name,
                "namespace": pod.metadata.namespace,
                "container": container.name,
                "image": container.image,
                "privileged": getattr(security, "privileged", False) if security else False,
                "run_as_user": getattr(security, "run_as_user", None) if security else None
            })
    return pod_data