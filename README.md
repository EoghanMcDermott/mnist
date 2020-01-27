# Using Tensorflow 2.0 to recognise MNIST handwritten digits

### A simple project used to get familiar with Tensorflow 2.0 and create a model that recognises handwritten digits based on the classic MNIST dataset

Running main.py gave the following results:
(Note, due to the inherent randomness in initialising weights etc, running this code yourself/repeatedly may give slightly different results)

```
    Train on 60000 samples, validate on 10000 samples
    Epoch 1/5
    60000/60000 [==============================] - 2s 33us/sample - loss: 0.3040 - accuracy: 0.9108 - val_loss: 0.1495 - val_accuracy: 0.9553
    Epoch 2/5
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.1496 - accuracy: 0.9554 - val_loss: 0.1030 - val_accuracy: 0.9691
    Epoch 3/5
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.1104 - accuracy: 0.9667 - val_loss: 0.0882 - val_accuracy: 0.9723
    Epoch 4/5
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.0908 - accuracy: 0.9720 - val_loss: 0.0780 - val_accuracy: 0.9766
    Epoch 5/5
    60000/60000 [==============================] - 2s 30us/sample - loss: 0.0777 - accuracy: 0.9760 - val_loss: 0.0726 - val_accuracy: 0.9788
```

## TODO: Add better visualisation