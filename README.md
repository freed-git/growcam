## docker

```
docker build -t deepvoid/trace-cli -f apps/trace-cli/Dockerfile apps/trace-cli/
```

# growcam

sudo raspi-config --expand-rootfs

sudo reboot

## install opencv

sudo apt update
sudo apt install python3-opencv

python3 -c 'import cv2; print(cv2.__version__)'

# windows

## Address in use

```
netstat -ano | findstr :5555
tasklist /svc /FI "PID eq <pid>"
stop-process <pid>
```

## test server listening on port

```
tnc 127.0.0.1 -port 5555
```

## for git on windows to use lf

```
git config --global core.eol lf
git config --global core.autocrlf false
git config --global core.autocrlf input
```