import streamlit as st
from volunteer_grants_engine import ModelParams, run_model

st.set_page_config(page_title="Volunteer Grants Allocation Model", layout="wide")
st.title("Volunteer Grants Allocation Model")
st.caption("Volunteer Grants only · Streamlit web front end")

with st.sidebar:
    st.header("Model settings")
    total_budget = st.number_input("Total budget", min_value=0.0, value=66000.0, step=1000.0)
    protected_threshold = st.number_input("Protected threshold", min_value=1000.0, value=1300.0, step=50.0)
    min_application = st.number_input("Minimum application", min_value=0.0, value=1000.0, step=50.0)
    haircut_mode = st.selectbox("Haircut mode", ["percentage", "cap"])
    haircut_rate = st.slider("Haircut rate", 0.0, 0.5, 0.10, 0.01)
    soft_cap = st.number_input("Soft cap", min_value=1000.0, value=4500.0, step=100.0)
    penalty_weight = st.slider("Penalty weight", 0.0, 1.0, 0.25, 0.01)
    st.subheader("Historical year weights")
    year_weight_2023_24 = st.slider("2023–24 weight", 0.0, 1.0, 0.35, 0.01)
    year_weight_2024_25 = st.slider("2024–25 weight", 0.0, 1.0, 0.65, 0.01)
    round_to_dollar = st.checkbox("Round allocations to whole dollars", value=True)
    st.markdown("---")
    historic_file = st.file_uploader("Upload historic awards workbook", type=["xlsx"])
    current_file = st.file_uploader("Upload current applicants workbook", type=["xlsx"])

if historic_file is None or current_file is None:
    st.info("Upload both workbooks in the sidebar to run the model.")
    st.stop()

params = ModelParams(total_budget, min_application, protected_threshold, haircut_mode, haircut_rate, soft_cap, penalty_weight, year_weight_2023_24, year_weight_2024_25, round_to_dollar)

try:
    outputs = run_model(historic_file, current_file, params)
except Exception as e:
    st.error(f"Model error: {e}")
    st.stop()

diag = outputs["diagnostics"].set_index("Diagnostic")["Value"]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Protected spend", f"${float(diag['Protected spend']):,.0f}")
c2.metric("Remaining budget", f"${float(diag['Remaining budget after protected spend']):,.0f}")
c3.metric("Fair total", f"${float(diag['Fair total']):,.0f}")
c4.metric("Dynamic total", f"${float(diag['Dynamic total']):,.0f}")

tabs = st.tabs(["Allocation Results","Method Comparison","Diagnostics","Penalty Impact","Validation","Duplicates / ABNs","Downloads"])
with tabs[0]:
    st.dataframe(outputs["results"], use_container_width=True)
with tabs[1]:
    st.dataframe(outputs["method_comparison"], use_container_width=True)
with tabs[2]:
    st.dataframe(outputs["diagnostics"], use_container_width=True)
    st.dataframe(outputs["parameters"], use_container_width=True)
with tabs[3]:
    st.dataframe(outputs["penalty_impact"], use_container_width=True)
with tabs[4]:
    st.dataframe(outputs["validation"], use_container_width=True)
with tabs[5]:
    st.subheader("Duplicate review")
    st.dataframe(outputs["duplicate_review"], use_container_width=True)
    st.subheader("ABN flags")
    st.dataframe(outputs["abn_flags"], use_container_width=True)
with tabs[6]:
    st.download_button("Download XLSX export", data=outputs["excel_bytes"], file_name="Volunteer_Grants_Allocation_Model_Streamlit_Output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    st.download_button("Download allocation results CSV", data=outputs["results"].to_csv(index=False).encode("utf-8"), file_name="allocation_results.csv", mime="text/csv")
