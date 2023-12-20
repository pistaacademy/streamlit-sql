import streamlit as st
import pandas as pd

import sqlite3
conn = sqlite3.connect('./world.sqlite')
c = conn.cursor()

def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data

def main():
    st.title("SQL Playground")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home Page")

        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQl Code Here")
                submit_code = st.form_submit_button("Execute")
        with col2:
            if submit_code:
                st.info("Query Submited")
                st.code(raw_code)
                query_results = sql_executor(raw_code)
                with st.expander("results"):
                    st.write(query_results)
                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)
            
    else:
        st.subheader("About")



if __name__ == '__main__':
    main()