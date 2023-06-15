#!/bin/bash
xhost +
docker run --gpus=all --rm -it \
 --shm-size=16gb \
 -v `pwd`:/project \
 -v /efs:/Datasets \
 -v /efs:/efs \
 -v /bigdata:/bigdata \
 -v /scratch:/scratch \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -v `pwd`/docker_history.txt:/root/.bash_history \
 -e DISPLAY=$DISPLAY \
 -h $HOSTNAME \
 --privileged \
 kylevedder/zeroflow_waymo:latest
