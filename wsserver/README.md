docker build -t deepvoid/wsserver -f wsserver/Dockerfile wsserver
docker push deepvoid/wsserver
docker run --rm -it -p 32080:80 deepvoid/wsserver
kubectl apply -f wsserver/manifests
kubectl delete -f wsserver/manifests
nc -zv localhost 32080
