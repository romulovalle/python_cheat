import numpy as np

# 1. Criando um array NumPy
print("1. Criando um array NumPy:")
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print()

# 2. Acessando elementos do array
print("2. Acessando elementos do array:")
print("Primeiro elemento:", array[0, 0])
print("Última linha:", array[-1])
print()

# 3. Calculando estatísticas básicas
print("3. Calculando estatísticas básicas:")
print("Média:", np.mean(array))
print("Mínimo:", np.min(array))
print("Máximo:", np.max(array))
print()

# 4. Operações matemáticas
print("4. Operações matemáticas:")
print("Soma de todos os elementos:", np.sum(array))
print("Produto de todos os elementos:", np.prod(array))
print()

# 5. Gerando arrays com valores específicos
print("5. Gerando arrays com valores específicos:")
zeros_array = np.zeros((2, 3))
print("Array de zeros:")
print(zeros_array)
ones_array = np.ones((3, 2))
print("Array de uns:")
print(ones_array)
random_array = np.random.rand(2, 2)
print("Array com valores aleatórios:")
print(random_array)
print()

# 6. Reshape de arrays
print("6. Reshape de arrays:")
reshaped_array = np.reshape(array, (3, 2))
print("Array remodelado:")
print(reshaped_array)
print()

# 7. Operações de álgebra linear
print("7. Operações de álgebra linear:")
transpose_array = np.transpose(array)
print("Transposta do array:")
print(transpose_array)
print("Produto interno de matrizes:")
matrix_product = np.dot(array, transpose_array)
print(matrix_product)
print()

# 8. Selecionando dados com base em condições
print("8. Selecionando dados com base em condições:")
print("Elementos maiores que 3:")
print(array[array > 3])
print()

# 9. Salvando e carregando arrays
print("9. Salvando e carregando arrays:")
np.save('array.npy', array)
loaded_array = np.load('array.npy')
print("Array carregado:")
print(loaded_array)
