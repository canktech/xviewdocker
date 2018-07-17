#!/usr/bin/env bash

# Installing new version of git on ubuntu:16.04 so that mxnet subdirs can be cloned correctly
apt-get -y update && apt-get -y install software-properties-common
add-apt-repository -y ppa:git-core/ppa && apt-get -y update && apt-get -y install git && git --version
