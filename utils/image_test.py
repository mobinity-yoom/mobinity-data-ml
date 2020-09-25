import tensorflow.compat.v1 as tf
import glob, os.path

# 검사하고자 하는 디렉토리 
for i, image_name in enumerate(glob.glob(os.path.join('./images', '*.jpeg'))):
    print(i, image_name)
    with tf.Graph().as_default():
        image_contents = tf.read_file(image_name)
        image = tf.image.decode_jpeg(image_contents, channels = 3)
        with tf.Session() as sess:
            # sess.run(init_op)
            sess.run(tf.global_variables_initializer())
            tmp = sess.run(image)
