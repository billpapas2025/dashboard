import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título del dashboard
st.title('Dashboard Matemático Avanzado')

# Opciones del menú lateral
option = st.sidebar.selectbox(
    'Seleccione un algoritmo:',
    ('Búsqueda Binaria', 'Números Primos', 'Máximo Común Divisor (MCD)', 'Secuencia de Fibonacci')
)

# Función para la búsqueda binaria
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Función para calcular los primeros números primos
def prime_numbers(n):
    primes = []
    num = 2
    while len(primes) < n:
        for i in range(2, int(np.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

# Función para calcular el MCD usando el Algoritmo de Euclides
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para generar la secuencia de Fibonacci
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Contenido según la opción seleccionada
if option == 'Búsqueda Binaria':
    st.subheader('Búsqueda Binaria')
    arr_input = st.text_input('Ingrese una lista ordenada de números separados por espacios:')
    x = st.number_input('Ingrese el número a buscar:', step=1)
    
    if st.button('Buscar'):
        if arr_input:
            try:
                arr = list(map(int, arr_input.split()))
                arr.sort()  # Asegurarse de que la lista esté ordenada
                index = binary_search(arr, int(x))
                if index != -1:
                    st.success(f'El número {x} está en la posición {index}.')
                else:
                    st.error(f'El número {x} no está en la lista.')
            except ValueError:
                st.error('Por favor, ingrese una lista válida de números enteros separados por espacios.')
        else:
            st.error('La lista de números no puede estar vacía.')

elif option == 'Números Primos':
    st.subheader('Números Primos')
    n = st.number_input('Ingrese la cantidad de números primos que desea calcular:', step=1)
    
    if st.button('Calcular'):
        if n > 0:
            primes = prime_numbers(int(n))
            st.write(f'Los primeros {int(n)} números primos son:')
            st.write(primes)
            # Graficar los números primos
            fig, ax = plt.subplots()
            ax.plot(primes, marker='o')
            ax.set_title(f'Gráfico de los primeros {int(n)} números primos')
            ax.set_xlabel('Índice')
            ax.set_ylabel('Números Primos')
            st.pyplot(fig)
        else:
            st.error('Por favor, ingrese un número mayor que 0.')

elif option == 'Máximo Común Divisor (MCD)':
    st.subheader('Máximo Común Divisor (MCD)')
    a = st.number_input('Ingrese el primer número:', step=1)
    b = st.number_input('Ingrese el segundo número:', step=1)
    
    if st.button('Calcular MCD'):
        if a > 0 and b > 0:
            result = gcd(int(a), int(b))
            st.success(f'El MCD de {int(a)} y {int(b)} es {result}.')
        else:
            st.error('Por favor, ingrese números mayores que 0.')

elif option == 'Secuencia de Fibonacci':
    st.subheader('Secuencia de Fibonacci')
    n = st.number_input('Ingrese la cantidad de términos que desea calcular:', step=1)
    
    if st.button('Calcular'):
        if n > 0:
            fib_seq = fibonacci(int(n))
            st.write(f'Los primeros {int(n)} términos de la secuencia de Fibonacci son:')
            st.write(fib_seq)
            # Graficar la secuencia de Fibonacci
            fig, ax = plt.subplots()
            ax.plot(fib_seq, marker='o')
            ax.set_title(f'Gráfico de los primeros {int(n)} términos de la secuencia de Fibonacci')
            ax.set_xlabel('Índice')
            ax.set_ylabel('Fibonacci')
            st.pyplot(fig)
        else:
            st.error('Por favor, ingrese un número mayor que 0.')
