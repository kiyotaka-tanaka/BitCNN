import tensorflow as tf
import numpy as np
import cPickle

def load_cifar_10(data_path):
    with open(data_path,"rb") as fopen:
        dictionary = cPickle.load(fopen)
    return dictionary["data"],dictionary["labels"]



