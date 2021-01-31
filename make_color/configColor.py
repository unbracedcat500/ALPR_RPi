# Copyright © 2019 by Spectrico
# Licensed under the MIT License

model_file = "/home/pi/Github/ALPR_RPi/make_color/model-weights-spectrico-car-colors-mobilenet-224x224-052EAC82.pb"  # path to the car color classifier
label_file = "/home/pi/Github/ALPR_RPi/make_color/labelColor.txt"   # path to the text file, containing list with the supported makes and models
input_layer = "input_1"
output_layer = "softmax/Softmax"
classifier_input_size = (224, 224) # input size of the classifier
