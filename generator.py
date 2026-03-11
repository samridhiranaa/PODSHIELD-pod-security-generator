import yaml

def generate_policy(image, allow_root):

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
                    "securityContext": {
                        "runAsNonRoot": not allow_root,
                        "readOnlyRootFilesystem": True,
                        "allowPrivilegeEscalation": False
                    }
                }
            ]
        }
    }

    return yaml.dump(policy)