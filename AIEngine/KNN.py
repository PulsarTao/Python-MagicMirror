# -*- coding: utf-8 -*-
'''
Created on 2016年8月1日

@author: VVAction
'''

from numpy import *

class K(object):
    '''
    classdocs
    '''
    dataMat=[]
    def __init__(self, filename):
        '''
        Constructor
                     构造函数如果类构造时代入文件路径
                     则读取分类文件数据矩阵
        '''
        if filename != None:
            fileMat=open(filename)
            for line in fileMat.readlines():
                curline=line.strip().split("\t")
                fltline=map(float,curline)
                self.dataMat.append(fltline)
                
    def distEclud(self,vecA,vecB):
        return sqrt (sum(power(vecA-vecB,2)))
    
    def randCent(self,dataset,k):
        '''
                     构建分类簇质心
        '''
        n=shape(dataset)[1]
        centroids=mat(zeros((k,n)))
        for j in range(n):
            minJ=min(dataset[:,j])
            rangeJ=float(max(dataset[:,j])-minJ)
            centroids[:,j]=minJ+rangeJ * random.rand(k,1)
        return centroids
    def KMeans(self,dataset,k,distMeas=distEclud,creatCent=randCent):
        '''
        K近邻算法
        '''
        m=shape(dataset)[0]
        clusterAssment=mat(zeros(m,2))
        centroids=creatCent(dataset,k)
        clusterChanged=True
        while clusterChanged:
            clusterChanged=False
            for i in range(m):
                minDist=inf.minIndex=-1
                '''
                                          寻找最近的近邻值
                '''
                for j in range(k):
                    distJI=distMeas(centroids[j,:],dataset[i,:])
                    if distJI < minDist:
                        minDist=distJI;minIndex=j
                if clusterAssment[i,0]!=minIndex:
                    clusterChanged=True
                clusterAssment[i,:]=minIndex,minDist**2
            print centroids
            '''
                                更新分类近似度
            '''
            for cent in range(k):
                ptsInClust=dataset[nonzero(clusterAssment[:,0].A==cent)[0]]
                centroids[cent,:]=mean(ptsInClust,axis=0)
        return centroids,clusterAssment
        