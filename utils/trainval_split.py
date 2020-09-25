
import tensorflow.compat.v1 as tf
import os
import glob
import logging

flags = tf.app.flags
flags.DEFINE_float('train_ratio', 0.8, 'Ratio of the training set')
flags.DEFINE_string('data_dir', '', 'Image data Directory')
FLAGS = flags.FLAGS

def main():
    train_ratio = FLAGS.train_ratio
    data_dir = FLAGS.data_dir

    random.seed(42)
    datas = os.listdir(data_dir)
    num_data = len(datas)
    num_train = int(train_ratio * num_data)
    train_img = datas[:num_train]
    val = datas[num_train:]
    logging.info('%d training and %d validation examples.',
               len(train), len(val))
    
    
    for i in train_xml:
        image_file = './data/trainval/' + i.split('.')[0] + '.jpeg'
        shutil.move(image_file, './train/')
        shutil.move('./data/trainval_annotation/' + i, './train/')

    for i in val_xml:
        image_file = './data/trainval/'+i.split('.')[0]+'.jpeg'
        shutil.move(image_file, './validation/')
        shutil.move('./data/trainval_annotation/'+i, './validation/')