
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("📊 Core System Data Explorer")

# Load metadata
table_df = pd.read_csv("table_structure.csv")
rel_df = pd.read_csv("table_relationships.csv")

# Sidebar - Table selection
tables = sorted(table_df["Table"].unique())
selected_table = st.sidebar.selectbox("Select a table to explore:", tables)

# Show columns for selected table
st.subheader(f"Columns in {selected_table}")
columns = table_df[table_df["Table"] == selected_table]["Column"].tolist()
st.write(columns)

# Show related tables
st.subheader("Related Tables")
related = rel_df[(rel_df["Table_A"] == selected_table) | (rel_df["Table_B"] == selected_table)]
if not related.empty:
    related["Related_Table"] = related.apply(lambda row: row["Table_B"] if row["Table_A"] == selected_table else row["Table_A"], axis=1)
    st.dataframe(related[["Related_Table", "Shared_Column"]].drop_duplicates())
else:
    st.write("No direct relationships found.")
