# StreamDataMbient
Streaming Data from Mbient sensors

Fall is one of the most common causes of accidental health. Elderly are more to falling when compared to others. So a cheaper aletrnative is required which can be implemented in retirement and nursing homes. In this project we built a real time fall detection system using Apache Flink and an advanced neural network model like Long Short Term Memory (LSTM) network. More information on the dataset used to train and different machine learning models is in Fall-Detection repository.

We used MetaMotionR device from MbientLab to collect raw accelrometer values. This data is sent to an edge device like laptop through a C# app developed using MbientLab SDK's. The data is sent from this app to Apache Flink where basic analysis is done. If the magnitude of the accelerometer values exceeds a certain threshold, a 10 second window of data is fed to the neural network model to classify if its a fall or not.
