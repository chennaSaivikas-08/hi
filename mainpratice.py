import streamlit as st
Pages={
    "Theorems":[
        st.Page("practice1.py",title="Theven's therom"),
        st.Page("Firstprogram.py",title="nortons therom"),
    ],
}
pg=st.navigation(Pages)
pg.run()
