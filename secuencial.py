import random
import time
import multiprocessing

def how_many_max_values_sequential(ar):
    maxValue = 0
    for i in range(len(ar)):
        if i == 0:
            maxValue = ar[i]
        else:
            if ar[i] > maxValue:
                maxValue = ar[i]
    contValue = 0
    for i in range(len(ar)):
        if ar[i] == maxValue:
            contValue += 1
    
    return contValue

def how_many_max_values_parallel(val):
    if val == max(ar):
        return 1
    else:
        return 0

if __name__ == '__main__':
    ar_count = 4000
    #ar = [4,4,3,1,30]
    ar = [random.randrange(1,30) for i in range(ar_count)]
    inicioSec = time.time()
    resultSec = how_many_max_values_sequential(ar)
    finSec =  (time.time()-inicioSec)*1000
    inicioPar = time.time()   
    pool      = multiprocessing.Pool(processes=4)
    resultPar = sum(list(pool.map(how_many_max_values_parallel,ar)))
    pool.close() 
    pool.join()
    finPar = (time.time()-inicioPar)*1000
    print('Results are correct!\n' if resultPar == resultSec else 'Results are incorrect!\n')

    print('Sequential Process took %.3f ms with %d items\n' % (finSec, ar_count))

    print('Parallel Process took %.3f ms with %d items\n' % (finPar, ar_count))
    print('Results are correct!\n' if finPar < finSec else 'Results are incorrect!\n')
