# examen

## Multiprocessing

**Comando :** python VegaMoreno_Bryam_ExamenMultiprocessing.py 


Para relizar el proceso de multiprocessing se realizo lo siguiente:

 * Se tomo en cuenta que se debio hacer en lotes debido a lo demorado del multiproceso
 * Continuando el método en paralelo para el máximo, es el mismo que en secuencial con la diferencia de que en multiproceso retorno un valor respuesta como resultado del proceso que realiza el método
 * En el método principal, el main, se toma en cuenta que se hace por lotes, el cual es un for en donde primero se instancia la variable de retorno resultado.
 * Dentro del mismo for instanciamos la variable process la cual va a ser la encargada de hacer el multiproceso, llamamos al método mediante el parametro tag y pasamos los argumentos mediante el parametro args
 * El parametro args pasamos la lista ar pero como podemos notar pasamos simplemente un rango que va desde un inicio hasta un salto
 * Despues iniciamos el proceso y unimos
 * Cotinuando con eso procedemos a cambiar el inicio por el salto y sumamos el salto más lo que debamos sumar para alcanzar el rango final
 * por ultimo en resultPar sumamos el lo que tenga la variable resultado(es lo que se retorno del método paralelo)
 * Un dato interesante es que este multiproceso trabajo bien con número de procesadores menores al número de procesadores totales que tiene la máquina, es decir que si mi máquina tiene 4 nucleos, este algoritmo trabaja bien cuando uso el multiproceso con nucles menores a 3, es decir, que cuando uso el multiprocessing con 4 nucleos, el tiempo aumenta, mientras que cuando uso con 4 o menos, el tiempo disminuye, esto hablando al momento de realizar los lotes, ya que el multiproceso dentro del for del lote trabajo con los 4 nucleos.

## MPI
**Comando :** mpiexec -n 8 python3 VegaMoreno_Bryam_ExamenMultiprocessing.py 
Para realizar el proceso de MPI se realizo lo siguiente:
 * Se realizo de la misma manera que en el trabajo anterior de multiplicación de matrices
 * Se instanciarón variables de FROM_MASTER Y FROM_WORKER la una es para verificar los tag o los id cuando haga los send y recive del mpi.
 * Después de ello se crea el vector de números randómicos como se especifíca en el examen
 * Una vez hecho eso instanciamos el MPI, obtenemos el número de trabajadores y el rank (proceso maestro)
 * despues de ello hacemos una resta del número de trabajadores debido a que de los 4 procesos 1 es el maestro y los otros son los trabajadores
 * una vez hecho eso realizamos un if en donde si es el maestro lo que va a realizar no es más que la división de vectores, para eso tenemos la variable averrow que divide la longitud del arreglo para el número de trabajadores, después un residuo que sera usado en caso de que la división sea impar, offset que me permitira obtener los rangos iniciales y mtype que es el id del tag del send y recive del mpi
 * Una vez intanciado las variables hacemos un for para el número de trabajadores y vemos si el dest+1 es menor o igual al residuo, si se cumple, entonces los rows son impares por tanto se le suma el averrow más 1, caso de que no,se deja el averrow
 * Enviamos los send en donde mando el offset(rango inicial), rows(salto),ar[offset:rows+offset](vector dividido)
 * suamos el offest más el row para que vaya dividiendo bien caso contrario siempre dividira solo el inicio del vector
 * Pasamos a los trabajadores, ellos seran los encargados de recivir los valores del maestro para eso esta un if en donde si el rank ya no es 0 entonces pues que reciva los valores del maestro y haga el proceso para calcular el máximo, después mando de la misma manera  el offset, rows y ahora solo mando el countValue que es el conteo de valores del maximo y otra cosa más, también se cambia el mtype ya que son trabajadores ahora.
 * Por ultimo los trabajadores reciben los resultados y solamente suman a la variable resultPar
 
  
## Resultados
#### Resultado de multiprocessing
![Alt text](procesos.png?raw=true "Procesos")
#### Resultado de mpi
![Alt text](mpi.png?raw=true "Procesos")
 
 
