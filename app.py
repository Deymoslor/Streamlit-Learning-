"""

My first app
hers our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd


#Creando un Datafreme con Pandas
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#magia
df
#tabla
st.table(df)


dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)
#Pandas Styler
dataframe2 = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('columna %d' % i for i in range(20))
)
st.dataframe(dataframe2.style.highlight_max(axis=0))
st.table(dataframe2)

#draw charts and maps
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a','b','c']
)
st.line_chart(chart_data)
map_data = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

#Widgets
x = st.slider('x')
st.write(x, 'squared is', x * x)
st.text_input("Your name", key='name')
st.session_state.name

#on_change Demostration
def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046

def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046
col1, buff, col2 = st.columns([2, 4, 2])
with col1:
    pounds = st.number_input("Pounds: ", key="lbs",
                            on_change=lbs_to_kg)
with col2:
    kilograms = st.number_input("Kilograms: ", key="kg",
                                on_change=kg_to_lbs)
    
#Checkboxes
if st.checkbox('Show dataframe'):
    chart_data2=pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data2

#Selectbox
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option+1


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

"-------------------------------------"

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

#Show progress
import time
'Starting a long computation...'



def chargeBar():
    # Add a placeholder
    latest_iteration = st.empty() #crea un contenedor que puede ser cambiado con el tiempo sin que la pagina recargue.
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
    '...and now we\'re done!'

#left_column = st
if st.button('Press me to charge the bar!'):
    chargeBar()