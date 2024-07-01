import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

# Título del dashboard
st.title('Dashboard Matemático Avanzado')

# Opciones del menú lateral
option = st.sidebar.selectbox(
    'Seleccione un algoritmo:',
    ('Búsqueda Binaria', 'Números Primos')
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
            
            # Crear un DataFrame con los números primos
            df = pd.DataFrame({'Primos': primes})
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'Posición'}, inplace=True)
            
            # Crear un gráfico de Altair
            chart = alt.Chart(df).mark_line(point=True).encode(
                x='Posición',
                y='Primos'
            ).properties(
                title='Primeros N Números Primos'
            )
            
            st.altair_chart(chart, use_container_width=True)
        else:
            st.error('Por favor, ingrese un número mayor que 0.')
