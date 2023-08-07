import pickle
import streamlit as st

model=pickle.load(open('estimasi-mobil1.sav', 'rb'))

st.title('estimasi harga mobil bekas')

year=st.number_input('input tahun mobil')
mileage=st.number_input('input km mobil')
tax=st.number_input('input pajak mobil')
mpg=st.number_input('input konsumsi bbm mobil')
engineSize=st.number_input('input engine mobil')

predict=''

if st.button('estimasi harga'):
    predict=model.predict(
        [[year, mileage,tax,mpg,engineSize]]
    )
    st.write('estimasi harga mobil bekas dalam pons:', predict)
    st.write('estimasi harga mobil bekas dalam IDR(Juta):', predict*19000)