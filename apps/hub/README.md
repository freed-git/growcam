## docker

```
docker build -t deepvoid/hub -f apps/hub/Dockerfile apps/hub/

docker run --rm -it --entrypoint bash deepvoid/hub

docker push deepvoid/hub
```

## kubectl

```
kubectl apply -f apps/hub/manifests

kubectl rollout restart deployment hub
```

## bash

```
nc -zv 192.168.1.201 5555
```
