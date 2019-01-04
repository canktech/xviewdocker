# xviewdocker
Builds docker for modified version mxnet used in xviewdataset.org competition

Reproducible patching of base machine learning model repos with new cpu versions of special nn operators for xviewdataset competition

Aim of xviewdataset competition:

To achieve best performance on dense object detection (100 to 1000s of objects per satellite image) with inference constraints of 1 cpu core and 8G ram.
At the time of competition mxnet was the most optimised version in terms of memory usage and speed. 
Several interesting 2 stage object detectors based on mxnet were built on top of incompatible forks of the mxnet machine learning framework.
Also CPU versions of special GPU operators from these interesting object detectors had to be compiled into tip of mxnet to gain better inference performance. 

This repo provides an example of a pragmatic way to merge all the changes required to build a base to compare conflicting mxnet model repos.
Competition pressure => (got to prioritise model architecture evoution without wasting too much time rebasing!)
