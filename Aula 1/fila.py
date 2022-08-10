#Fila: são estruturas de dados em que só é possível inserir um novo elemento no final da fila e só é possível remover um elemento do início.


from collections import deque

fila = deque(['Morango', 'Banana', 'Uva'])

fila.append('Amora')

head = fila.popleft() #Remove Morango

print(fila, head) #deque(['Banana', 'Uva', 'Amora']) Morango
