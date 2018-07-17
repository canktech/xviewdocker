# beginning of real docker stuff
FROM ubuntu:16.04

COPY install/cpp.sh install/
RUN install/cpp.sh
COPY install/git.sh install/
RUN install/git.sh

RUN git clone --recursive https://github.com/apache/incubator-mxnet
COPY patches/incubator-mxnet incubator-mxnet
RUN cd incubator-mxnet && git diff && \
     make -j$(nproc) && rm -r build

COPY install/python.sh install/
RUN install/python.sh
ENV  PYTHONPATH=/incubator-mxnet/python

RUN git clone https://github.com/msracver/Deformable-ConvNets
COPY patches/Deformable-ConvNets Deformable-ConvNets
RUN cd Deformable-ConvNets && git diff && \
     pip install -r requirements.txt && \
     chmod +x init.sh && ./init.sh && python ./rfcn/demo.py --cpu_only


