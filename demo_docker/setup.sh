#!/usr/bin/env bash


# Check update for docker
docker pull calee/kaib-cpu


# Docker path
docker_absolute_path=/data/kenkim/kaib_NIPS

sudo docker run -w /app/demo_docker -p 1990:1990 -v $docker_absolute_path:/app calee/kaib-cpu python -u run-demo-simple.py
