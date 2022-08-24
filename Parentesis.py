
#Análisis
#'()[]{}'=> True
#'()[}'  S=> False

def cadena_parentesis(problema): #creamos el nombre de la función y nombramos a problema como tipo string, ese sería el único argumento. 
    pila = [] #se crea una lista llamada pila
    parentesis = {'{':'}','(':')','[':']'}  #funciona como un diccionario y se llama parentesis
    # y para mostrar como es que tiene que estar el valor como llave de apertura y cierre

    for c in problema: #se hace un ciclo for usando el estilo de c
        if c in parentesis: #si el caracter actual se encuentra dentro del conjunto de parentesis
            pila.append(c) # append Agrega un ítem al final de la lista, si se cumple la condición. 
        elif  len(pila) == 0 or c != parentesis[pila.pop()]:#si la lista pila se encuentra vacia o c es distinto al parentesis, se accede al arregloy se extrea el último elemento que se agrego
            return False # si ese es el caso se devuelve false
    return len(pila) == 0  #cuando ternime las interaciones, se pregunta si la pila esta vacia, si esta vacia se retorna true. 

problema4 = "([[{}{}]()])" #true
problema3 = "([[{}{})()])" #false
problema2 = "([{}])" #true
problema= "([[{}])" #false



print(cadena_parentesis(problema3))

