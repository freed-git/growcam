## docker

```
docker build -t deepvoid/webserver -f apps/webserver/Dockerfile apps/webserver/

docker run --rm -it --entrypoint bash deepvoid/webserver

docker push deepvoid/webserver
```

## kubectl

```
kubectl apply -f apps/webserver/manifests -n growcam

kubectl rollout restart deployment webserver -n growcam
```

## bash

```
nc -zv 192.168.1.201 5555
```
