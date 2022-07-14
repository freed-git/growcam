from kubernetes import client, config
config.load_kube_config()
v1 = client.CoreV1Api()

endpoint = v1.read_namespaced_endpoints(namespace='default', name='pub-headless')

for subset in endpoint.subsets:
    for address in subset.addresses:
        print(f'ip: {address.ip}, hostname: {address.hostname}')

# pods = v1.list_namespaced_pod(namespace='default', label_selector='app=pub')
# for pod in pods.items:
#     print(pod.metadata.name)
# print(pods)