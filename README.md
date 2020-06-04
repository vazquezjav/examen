# examen

## Multiprocessing

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

Para realizar el proceso de MPI se realizo lo siguiente:
 *Se realizo de la misma manera que en el trabajo anterior de multiplicación de matrices
 
