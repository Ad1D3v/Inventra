import asyncio
import streamlit as st

# Handle the LangChain-Streamlit Sync
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# Import Chain from Custom Module
from ivt_core import ivt_chain

# Define Page Setup
st.set_page_config(page_title="Inventra", page_icon="📋")
st.title("Inventra")
st.subheader("Smarter Inventory, Smoother Operations.")

# Define Interface Elements
ivt_query = st.text_area("How can I help you..?")
ivt_ask = st.button("Ask Inventra")

# Handle User Input
if ivt_ask:
    if ivt_query is None or ivt_query == "":
        st.info(".. .. Please enter a valid Query you may have ...⚠️⚠️⚠️")

    else:
        with st.spinner("Evaluating Inventory...🔄🔄🔄"):
            result = ivt_chain.run(ivt_query)
        st.info("Inventory Evaluated!!...✅✅✅")
        st.markdown(result)