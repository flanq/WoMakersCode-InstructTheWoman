# Pilha: são estruturas de dados em que só é possível inserir um novo elemento no final da pilha e só é possível remover um elemento do final da pilha

from typing import List

stack: List[str] = []

stack.append('Banana')
stack.append('Kiwi')
stack.append('Morango')

print(stack) #['Banana', 'Kiwi', 'Morango']

top_item = stack.pop() 
print(top_item) # Morango

