import multiprocessing


import random
import time

resultPar = 0

def how_many_max_values_sequential(ar):

    #find max value of the list

    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]

    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1

    return contValue

 

# Complete the how_many_max_values_parallel function below.

def how_many_max_values_parallel(ar):
    
    #implement your solution'
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]

    #find how many max values are in the list
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    respuesta.value = contValue
 

if __name__ == '__main__':
    ar_count = 40000000
    #Generate ar_count random numbers between 1 and 30
    ar = [random.randrange(1,30) for i in range(ar_count)]
    inicioSec = time.time()
    resultSec = how_many_max_values_sequential(ar)
    finSec =  time.time()
    inicioPar = time.time()   
    inicio = 0
    salto = 10000000
    for i in range(3): 
        respuesta= multiprocessing.Value("i", 0)
        process = multiprocessing.Process(target=how_many_max_values_parallel,args = (ar[inicio:salto],))
        process.start()
        process.join()
        inicio = salto
        salto = salto+10000000
        resultPar=resultPar+respuesta.value
    finPar = time.time()

   

    print('Results are correct!\n' if resultSec == resultPar else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % ((finSec - inicioSec)*1000, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % ((finPar - inicioPar)*1000, ar_count))
