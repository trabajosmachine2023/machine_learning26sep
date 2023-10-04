import streamlit as st
import numpy as np 
import pandas as pd 
import pickle 
from catboost import CatBoostRegressor
import sklearn

with open ("model.pkl","rb") as doc:
    model=pickle.load(doc)

st.title("Modelo")
st.divider()
st.write("Digite los datos")

assess=st.slider("Assess",0,100000)
bedrooms=st.slider("Bedrooms",0,50)
lotsize=st.slider("Lote Size",0,900000)
square_fit=st.slider("Square Fit",0,1000000)
colonial=st.selectbox("Colonial",[0,1])


prediccion=model.predict(np.array([[assess,bedrooms,lotsize,square_fit,colonial]]))
if st.button("Generar precio"):
    st.write(f"El precio de la vivienda es de {prediccion[0]}")

