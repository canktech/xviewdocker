# --------------------------------------------------------
# Deformable Convolutional Networks
# Copyright (c) 2017 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Yi Li, Haocheng Zhang
# --------------------------------------------------------

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from random import random as rand
 
num_classes = 101
cmap = {i: (rand(),rand(),rand()) for i in range(num_classes)} 
def show_boxes(im, dets, classes, scale = 1.0, name="demo.png"):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.cla()
    ax.axis("off")
    plt.imshow(im)
    for cls_idx, cls_name in enumerate(classes):
        cls_dets = dets[cls_idx]
        for det in cls_dets:
            bbox = det[:4] * scale
            color = cmap[cls_idx]
            rect = plt.Rectangle((bbox[0], bbox[1]),
                                  bbox[2] - bbox[0],
                                  bbox[3] - bbox[1], fill=False,
                                  edgecolor=color, linewidth=2.5)
            ax.add_patch(rect)

            if cls_dets.shape[1] == 5:
                score = det[-1]
                ax.text(bbox[0], bbox[1],
                               '{:s} {:.3f}'.format(cls_name, score),
                               bbox=dict(facecolor=color, alpha=0.5), fontsize=9, color='white')
    fig.savefig(name)
    return im

