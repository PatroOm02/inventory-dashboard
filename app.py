
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    par_level_df = pd.read_csv("par_level_recommendations.csv")
    sim_df = pd.read_csv("inventory_simulation_results.csv")
    weekly_df = pd.read_csv("filtered_weekly.csv", parse_dates=['Date'])
    for df in [par_level_df, sim_df, weekly_df]:
        df['Bar Name'] = df['Bar Name'].str.strip()
        df['Brand Name'] = df['Brand Name'].str.strip()
    return par_level_df, sim_df, weekly_df

par_level_df, sim_df, weekly_df = load_data()

st.sidebar.title("Inventory Forecasting Dashboard")
bars = par_level_df['Bar Name'].unique()
brands = par_level_df['Brand Name'].unique()
selected_bar = st.sidebar.selectbox("Select Bar", bars)
selected_brand = st.sidebar.selectbox("Select Brand", brands)
st.title(f"📦 Inventory Insights: {selected_brand} @ {selected_bar}")

par_row = par_level_df[(par_level_df['Bar Name'] == selected_bar) & (par_level_df['Brand Name'] == selected_brand)]
sim_row = sim_df[(sim_df['Bar Name'] == selected_bar) & (sim_df['Brand Name'] == selected_brand)]
time_series = weekly_df[(weekly_df['Bar Name'] == selected_bar) & (weekly_df['Brand Name'] == selected_brand)]

if not par_row.empty and not sim_row.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Par Level (ml)", round(par_row['Recommended Par Level (ml)'].values[0], 2))
    col2.metric("Stockout %", f"{sim_row['Stockout %'].values[0]}%")
    col3.metric("Overstock (ml)", round(sim_row['Total Overstock (ml)'].values[0], 2))
else:
    st.warning("⚠️ Simulation or par level data not found for this Bar/Brand.")

st.subheader("📉 Weekly Net Usage (ml)")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=time_series, x='Date', y='Net Usage (ml)', marker='o', ax=ax)
if not par_row.empty:
    par_val = par_row['Recommended Par Level (ml)'].values[0]
    ax.axhline(par_val, color='red', linestyle='--', label='Par Level')
    ax.legend()
ax.set_title(f"Demand vs Par Level - {selected_brand}")
ax.set_ylabel("Net Usage (ml)")
ax.set_xlabel("Date")
ax.tick_params(axis='x', rotation=45)
plt.xticks(ha='right')
plt.tight_layout()
st.pyplot(fig)

if not sim_row.empty:
    with st.expander("📋 Full Simulation Stats"):
        st.dataframe(sim_row.reset_index(drop=True))
else:
    st.info("ℹ️ No simulation results available for this combination.")
