#!/usr/bin/env python3   #?
# -*- coding: utf-8 -*-   #говорим питону (или юпитеру?), что будем использовать кодировку UTF-8
 
import math #подключение модуля math
import numpy #подключение модуля numpy
import matplotlib.pyplot as mpp #подключение модуля matplotlib.pyplot в виде какого-то mpp


if __name__=='__main__': #лежит ли в переменной __name__ строка __main__
    arguments = numpy.r_[0:200:0.1] #цикл, переменная arguments меняется от 0 до 200 с шагом 0.1
    mpp.plot( # открытие чего-то, называющегося mpp.plot
        arguments, # ?
        [math.sin(a) * math.sin(a/20.0) for a in arguments] #?
    )  # закрытие чего-то, называющегося mpp.plot
    mpp.show() # видимо, показать значения, полученные в mpp.plot, на экране
