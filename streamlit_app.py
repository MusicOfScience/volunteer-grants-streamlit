import streamlit as st
from volunteer_grants_engine import APP_VERSION, ModelParams, run_model

st.set_page_config(page_title="Volunteer Grants Allocation Model", layout="wide")

DEFAULTS = {
    "total_budget": 66000.0,
    "min_application": 1000.0,
    "protected_threshold": 1300.0,
    "haircut_mode": "percentage",
    "haircut_rate": 0.10,
    "soft_cap": 4500.0,
    "penalty_weight": 0.25,
    "year_weight_2023_24": 0.35,
    "year_weight_2024_25": 0.65,
    "round_to_dollar": True,
}

if "confirmed_settings" not in st.session_state:
    st.session_state.confirmed_settings = DEFAULTS.copy()
if "budget_locked" not in st.session_state:
    st.session_state.budget_locked = False
if "pending_budget" not in st.session_state:
    st.session_state.pending_budget = st.session_state.confirmed_settings["total_budget"]
if "live_settings" not in st.session_state:
    st.session_state.live_settings = st.session_state.confirmed_settings.copy()

st.title(f"Volunteer Grants Allocation Model — {APP_VERSION}")
st.caption("Volunteer Grants only · eligibility-aware duplicate review · audit-focused export views")

with st.sidebar:
    st.header("Model settings")

    st.subheader("Budget")
    pending_budget = st.number_input(
        "Budget input",
        min_value=0.0,
        value=float(st.session_state.pending_budget),
        step=1000.0,
        key="budget_input_field"
    )
    st.session_state.pending_budget = pending_budget

    c1, c2 = st.columns(2)
    with c1:
        if st.button("Confirm / Lock budget", use_container_width=True):
            st.session_state.confirmed_settings["total_budget"] = float(st.session_state.pending_budget)
            st.session_state.live_settings["total_budget"] = float(st.session_state.pending_budget)
            st.session_state.budget_locked = True
    with c2:
        if st.button("Undo budget", use_container_width=True):
            st.session_state.pending_budget = st.session_state.confirmed_settings["total_budget"]
            st.rerun()

    if st.session_state.pending_budget != st.session_state.confirmed_settings["total_budget"]:
        st.warning("Budget input has changed but is not yet confirmed.")
        st.session_state.budget_locked = False
    else:
        st.success(f"Locked budget: ${st.session_state.confirmed_settings['total_budget']:,.0f}")

    st.markdown("---")
    st.subheader("Other settings")

    protected_threshold = st.number_input(
        "Protected threshold",
        min_value=1000.0,
        value=float(st.session_state.live_settings["protected_threshold"]),
        step=50.0,
    )
    min_application = st.number_input(
        "Minimum application",
        min_value=0.0,
        value=float(st.session_state.live_settings["min_application"]),
        step=50.0,
    )
    haircut_mode = st.selectbox(
        "Haircut mode",
        ["percentage", "cap"],
        index=["percentage", "cap"].index(st.session_state.live_settings["haircut_mode"]),
    )
    haircut_rate = st.slider(
        "Haircut rate",
        0.0, 0.5, float(st.session_state.live_settings["haircut_rate"]), 0.01
    )
    soft_cap = st.number_input(
        "Soft cap",
        min_value=1000.0,
        value=float(st.session_state.live_settings["soft_cap"]),
        step=100.0,
    )
    penalty_weight = st.slider(
        "Penalty weight",
        0.0, 1.0, float(st.session_state.live_settings["penalty_weight"]), 0.01
    )
    st.caption("Historical year weights control how strongly the older and more recent prior rounds influence the moderate history penalty.")
    year_weight_2023_24 = st.slider(
        "2023–24 weight",
        0.0, 1.0, float(st.session_state.live_settings["year_weight_2023_24"]), 0.01
    )
    year_weight_2024_25 = st.slider(
        "2024–25 weight",
        0.0, 1.0, float(st.session_state.live_settings["year_weight_2024_25"]), 0.01
    )
    round_to_dollar = st.checkbox(
        "Round allocations to whole dollars",
        value=bool(st.session_state.live_settings["round_to_dollar"])
    )

    st.session_state.live_settings.update({
        "protected_threshold": protected_threshold,
        "min_application": min_application,
        "haircut_mode": haircut_mode,
        "haircut_rate": haircut_rate,
        "soft_cap": soft_cap,
        "penalty_weight": penalty_weight,
        "year_weight_2023_24": year_weight_2023_24,
        "year_weight_2024_25": year_weight_2024_25,
        "round_to_dollar": round_to_dollar,
    })

    c3, c4 = st.columns(2)
    with c3:
        if st.button("Confirm other settings", use_container_width=True):
            for k in ["protected_threshold","min_application","haircut_mode","haircut_rate","soft_cap","penalty_weight","year_weight_2023_24","year_weight_2024_25","round_to_dollar"]:
                st.session_state.confirmed_settings[k] = st.session_state.live_settings[k]
    with c4:
        if st.button("Undo other settings", use_container_width=True):
            for k in ["protected_threshold","min_application","haircut_mode","haircut_rate","soft_cap","penalty_weight","year_weight_2023_24","year_weight_2024_25","round_to_dollar"]:
                st.session_state.live_settings[k] = st.session_state.confirmed_settings[k]
            st.rerun()

    if st.button("Revert all to last confirmed scenario", use_container_width=True):
        st.session_state.pending_budget = st.session_state.confirmed_settings["total_budget"]
        st.session_state.live_settings = st.session_state.confirmed_settings.copy()
        st.rerun()

    st.markdown("---")
    historic_file = st.file_uploader("Upload historic awards workbook", type=["xlsx"])
    current_file = st.file_uploader("Upload current applicants workbook", type=["xlsx"])

if historic_file is None or current_file is None:
    st.info("Upload both workbooks in the sidebar to run the model.")
    st.stop()

if not st.session_state.budget_locked:
    st.warning("The budget is not locked. Confirm / Lock budget before running the working scenario.")
    st.stop()

params = ModelParams(
    total_budget=st.session_state.confirmed_settings["total_budget"],
    min_application=st.session_state.live_settings["min_application"],
    protected_threshold=st.session_state.live_settings["protected_threshold"],
    haircut_mode=st.session_state.live_settings["haircut_mode"],
    haircut_rate=st.session_state.live_settings["haircut_rate"],
    soft_cap=st.session_state.live_settings["soft_cap"],
    penalty_weight=st.session_state.live_settings["penalty_weight"],
    year_weight_2023_24=st.session_state.live_settings["year_weight_2023_24"],
    year_weight_2024_25=st.session_state.live_settings["year_weight_2024_25"],
    round_to_dollar=st.session_state.live_settings["round_to_dollar"],
)

try:
    outputs = run_model(historic_file, current_file, params)
except Exception as e:
    st.error(f"Model error: {e}")
    st.stop()

diag = outputs["diagnostics"].set_index("Diagnostic")["Value"]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total requested", f"${float(diag['Total requested']):,.0f}")
c2.metric("Protected spend", f"${float(diag['Protected spend']):,.0f}")
c3.metric("Recommended total (Fair)", f"${float(diag['Fair total']):,.0f}")
c4.metric("Recommended total (Dynamic)", f"${float(diag['Dynamic total']):,.0f}")

st.markdown("### Proposed 2025–26 recommendation view")
method_choice = st.radio("Choose which recommendation method to display", ["Fair", "Dynamic"], horizontal=True)

if method_choice == "Fair":
    st.caption("Fair method: a flatter, more even distribution of the available money above the threshold floor, while still applying the moderate historical penalty.")
    st.dataframe(outputs["submission_view_fair"], use_container_width=True)
else:
    st.caption("Dynamic method: a more directly weighted distribution of the available money above the threshold floor, based on extra capacity and the moderate historical penalty.")
    st.dataframe(outputs["submission_view_dynamic"], use_container_width=True)

tabs = st.tabs([
    "Allocation Results",
    "Method Comparison",
    "Diagnostics",
    "Penalty Impact",
    "Eligibility & Duplicate Review",
    "Validation",
    "Downloads"
])

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
    st.subheader("Included in Model")
    st.dataframe(outputs["included_in_model"], use_container_width=True)
    st.subheader("Excluded by Eligibility")
    st.dataframe(outputs["excluded_by_eligibility"], use_container_width=True)
    st.subheader("Duplicate Review")
    st.dataframe(outputs["review_table"], use_container_width=True)

with tabs[5]:
    st.dataframe(outputs["validation"], use_container_width=True)

with tabs[6]:
    st.download_button(
        "Download XLSX export",
        data=outputs["excel_bytes"],
        file_name=f"Volunteer_Grants_Allocation_Model_{APP_VERSION}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.download_button(
        "Download allocation results CSV",
        data=outputs["results"].to_csv(index=False).encode("utf-8"),
        file_name=f"Volunteer_Grants_Allocation_Model_{APP_VERSION}.csv",
        mime="text/csv"
    )
