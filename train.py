import tensorflow as tf
from model import BitCNN
import argparse

import utils

parser = argparse.ArgumentParser()

parser.add_argument()
parser.add_argument()

args = parser.parse_args()

bithash = BitCNN()

bithash.train()
