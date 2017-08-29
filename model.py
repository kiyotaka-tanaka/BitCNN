import tensorflow as tf
import numpy as np 


class BitCNN:
    
    def __init__(self,batch_size,num_classes):

        self.batch_size = batch_size
        self.num_class = num_classes

        self.input_holder = tf.placeholder(tf.float32,[None,32,32,3])
        self.out_holder = tf.placeholder(tf.float32,[None,10])
        
        self.loss_network()

    def network(self):
        with tf.variable_scope("conv1"):
            out = tf.layers.conv2d(self.input_holder,filters=32,kernel_size=[5,5],strides=(1,1),padding="same")
            out = tf.layers.average_pooling2d(out,pool_size=(2,2),padding="same")
        with tf.variable_scope("conv2"):
            out = tf.layers.conv2d(out,filters=64,kernel_size=[5,5],strides=(1,1),padding="same")
            out = tf.layers.average_pooling2d(out,pool_size=(2,2),padding="same")
        with tf.variable_scope(conv3):
            out = tf.layers.conv2d(out,filters=128,kernel_size=[5,5],strides=(1,1),padding="same")
            out = tf.layers.average_pooling2d(out,pool_size=(2,2),padding="same")

        with tf.variable_scope("FC1"):
            out = tf.reshape(out,[-1,4*4*128])
            out = tf.layers.dense(out,512)
            out = tf.nn.relu(out)
        with tf.variable_scope("FC2"):
            out = tf.layers.dense(out,24)
            out = tf.nn.relu(out)
            
        ### tangent like relu to require bit hashing ###
        
    def loss_network(self):
        ### build loss function from ###
        pass

    def train(self):
        pass
