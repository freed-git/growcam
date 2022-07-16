docker build -t deepvoid/wsserver -f wsserver/Dockerfile wsserver
docker push deepvoid/wsserver
docker run --rm -it -p 32080:80 deepvoid/wsserver
kubectl apply -f wsserver/manifests
kubectl delete -f wsserver/manifests
kubectl rollout restart deploy wsserver

kubectl port-forward deployment/wsserver 32080:80

nc -zv localhost 32080
python -m websockets ws://localhost:32080/
time python benchmark.py 500 6
