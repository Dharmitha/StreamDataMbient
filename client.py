
import socket 
import sys
from statistics import median
from statistics import stdev
from scipy.stats import kurtosis,skew
import math
import numpy as np


def feature(realdata,j):
    final = []
    i=0
    while(i<500):
                test = []
                
                X = [float(realdata[k][1]) for k in range(i,i+50)]
                Y = [float(realdata[k][2]) for k in range(i,i+50)]
                Z = [float(realdata[k][3]) for k in range(i,i+50)]
                    
                MAG = [float(realdata[k][4]) for k in range(i,i+50)]
                ymag = [float(realdata[k][2])/float(realdata[k][4]) for k in range(i,i+50)]
                avgX = sum(X)/len(X)
                avgY = sum(Y)/len(Y)
                avgZ = sum(Z)/len(Z)
                medianX = median(X)
                medianY = median(Y)
                medianZ = median(Z)
                stdX = stdev(X)
                stdY = stdev(Y)
                stdZ = stdev(Z)
                skewX = skew(X)
                skewY = skew(Y)
                skewZ = skew(Z)
                kurtosisX = kurtosis(X)
                kurtosisY = kurtosis(Y)
                kurtosisZ = kurtosis(Z)
                minX = min(X)
                minY = min(Y)
                minZ = min(Z)
                maxX = max(X)
                maxY = max(Y)
                maxZ  = max(Z)
                slope = math.sqrt((maxX - minX)**2 + (maxY - minY)**2 + (maxZ - minZ)**2)
                TA = [math.asin(ymag[k]) for k in range(0,50)]
                meanTA = sum(TA)/len(TA)
                stdTA = stdev(TA)
                skewTA = skew(TA)
                kurtosisTA = kurtosis(TA)
                absX = sum([abs(X[k] - avgX) for k in range(0,50) ]) / len(X)
                absY = sum([abs(Y[k] - avgY) for k in range(0,50) ]) / len(Y)
                absZ = sum([abs(Z[k] - avgZ) for k in range(0,50) ]) / len(Z)
                abs_meanX = sum([abs(X[k]) for k in range(0,50)])/len(X)
                abs_meanY = sum([abs(Y[k]) for k in range(0,50)])/len(Y)
                abs_meanZ = sum([abs(Z[k]) for k in range(0,50)])/len(Z)
                abs_medianX = median([abs(X[k]) for k in range(0,50)])
                abs_medianY = median([abs(Y[k]) for k in range(0,50)])
                abs_medianZ = median([abs(Z[k]) for k in range(0,50)])
                abs_stdX = stdev([abs(X[k]) for k in range(0,50)])
                abs_stdY = stdev([abs(Y[k]) for k in range(0,50)])
                abs_stdZ = stdev([abs(Z[k]) for k in range(0,50)])
                abs_skewX = skew([abs(X[k]) for k in range(0,50)])
                abs_skewY = skew([abs(Y[k]) for k in range(0,50)])
                abs_skewZ = skew([abs(Z[k]) for k in range(0,50)])
                abs_kurtosisX = kurtosis([abs(X[k]) for k in range(0,50)])
                abs_kurtosisY = kurtosis([abs(Y[k]) for k in range(0,50)])
                abs_kurtosisZ = kurtosis([abs(Z[k]) for k in range(0,50)])
                abs_minX = min([abs(X[k]) for k in range(0,50)])
                abs_minY = min([abs(Y[k]) for k in range(0,50)])
                abs_minZ = min([abs(Z[k]) for k in range(0,50)])
                abs_maxX = max([abs(X[k]) for k in range(0,50)])
                abs_maxY = max([abs(Y[k]) for k in range(0,50)])
                abs_maxZ  = max([abs(Z[k]) for k in range(0,50)])
                abs_slope = math.sqrt((abs_maxX - abs_minX)**2 + (abs_maxY - abs_minY)**2 + (abs_maxZ - abs_minZ)**2)
                meanMag = sum(MAG)/len(MAG)
                stdMag = stdev(MAG)
                minMag = min(MAG)
                maxMag = max(MAG)
                DiffMinMaxMag = maxMag - minMag
                ZCR_Mag = 0
                AvgResAcc = (1/len(MAG))*sum(MAG)
                i = i+50
                test = [avgX,avgY,avgZ,medianX,medianY,medianZ,stdX,stdY,stdZ,skewX,skewY,skewZ,kurtosisX,kurtosisY,kurtosisZ,
                                      minX,minY,minZ,maxX,maxY,maxZ,slope,TA,meanTA,stdTA,skewTA,kurtosisTA,absX,
                                      absY,absZ,abs_meanX,abs_meanY,abs_meanZ,abs_medianX,abs_medianY,abs_medianZ,
                                      abs_stdX,abs_stdY,abs_stdZ,abs_skewX,abs_skewY,abs_skewZ,abs_kurtosisX,
                                      abs_kurtosisY,abs_kurtosisZ,abs_minX,abs_minY,abs_minZ,abs_maxX,abs_maxY
                                      ,abs_maxZ,abs_slope,meanMag,stdMag,minMag,maxMag,DiffMinMaxMag,ZCR_Mag,AvgResAcc]
                
                final.append(test)
    return final

def test():
    dataset = genfromtxt('features_l.csv', delimiter=',')

    ypredicted =  []

    for time in range(0,1):
        x = [lala[index] for index in range(0,10)]
        x = numpy.array(x)
        X = x.reshape(1, 10, (lala.shape[1]))
        yhat = model.predict(X,verbose=0)[0]
        print (yhat)
        for index1 in range(10):
            i = np.where(yhat[index1] == yhat[index1].max())
            hin = i[0]
            for index2 in range(2):
                if(index2==hin):
                    yhat[index1][index2]=1
                else:
                    yhat[index1][index2]=0
        j= yhat
        for index1 in range(10):
            ypredicted.append(j[index1])
         
    yp=[]
    for index1 in range(len(ypredicted)):
            if (ypredicted[index1][0]==1 and ypredicted[index1][1]==0 ):
                yp.append(0)
            if (ypredicted[index1][0]==0 and ypredicted[index1][1]==1 ):
                yp.append(1)
    
    print(yp)
    




host = '127.0.0.1' 
port = 9099
mySocket1 = socket.socket() 
mySocket1.connect((host,port)) 
realdata =[]
testdata = []
interdata =  []
X =[]
Y=[]
Z=[]
j=0
with open('features_l.csv','a') as f1:
  writer=csv.writer(f1, delimiter=',',lineterminator='\n',)
  writer.writerow(['AvgX','AvgY','AvgZ','MedianX','MedianY','MedianZ','StdX',
    'StdY','StdZ','SkewX','SkewY','SkewZ','KurtosisX','KurtosisY','KurtosisZ','MinX','MinY',
    'MinZ','MaxX','MaxY','MaxZ','Slope','MeanTA','StdTA','SkewTA','KurtosisTA',
    'AbsX','AbsY','AbsZ','AbsMeanX','AbsMeanY','AbsMeanZ','AbsMedianX','AbsMedianY','AbsMedianZ',
    'AbsStdX','AbsStdY','AbsStdZ','AbsSkewX','AbsSkewY','AbsSkewZ',
    'AbsKurtosisX','AbsKurtosisY','AbsKurtosisZ','AbsMinX','AbsMinY','AbsMinZ',
    'AbsMaxX','AbsMaxY','AbsMaxZ','AbsSlope','MeanMag',
    'StdMag','MinMag','MaxMag','DiffMinMaxMag','ZCR_Mag','AverageResultantAcceleration'])
  while(True):
    data = mySocket1.recv(1024) 
    d = str(data,'utf-8')
    da = d.split("\n")
    for ind in da:
        if(ind):
            daa = ind.split(",")
            realdata.append(daa)
            j=j+1
    if(j%500==0):
        
        lala = feature(realdata,j)
        
        for p in range(0,10):
                writer.writerow(lala[p])
                
        break
                
test()
                

mySocket1.close()
