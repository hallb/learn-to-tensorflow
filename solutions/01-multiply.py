## Lesson 1 - multiply 2 constants
# Write a simple Tensorflow program that has the following phases

import tensorflow as tf

## data
input1 = [[3. , 5.]]
input2 = [[7.],[1.]]

# Multiply a 1x2 [[3.,5.]] by a 2x1 [[7.],[1.]]
a = tf.constant( [[3. , 5.]] )
b = tf.constant( [[7.],[1.]] )


## induction
# Set up two constants to be multiplied
# Multiply a by b
c = tf.matmul(a,b)


## training
# Run tensorflow and print the result, the result should be 26
with tf.Session() as sess:
  print "Session started."
  result = sess.run(c)
  print "The result is",result
  print "Which is", ( "correct" if result == 26.0 else "incorrect" )
