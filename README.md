# 📦 Inventory Forecasting & Par Level Optimization Dashboard

This project is an intelligent inventory management system designed for a hotel chain operating multiple bars. The dashboard helps reduce **stockouts** of high-demand items and avoid **overstocking** of slow-moving brands by forecasting weekly demand and recommending optimal stock levels (Par Levels).

🔗 **Live App**: [Open Streamlit Dashboard](https://inventory-dashboard-tbjmqt9bubcghrhuo3d454.streamlit.app/)

---

## 🚀 Features

- 📊 Weekly demand forecasting (per bar and brand)
- ✅ Recommended Par Level with 95% service level buffer
- 🔍 Simulation of stockouts and overstock based on historical data
- 📈 Visual trend of consumption vs. par level
- 🧠 Smart, data-driven decision support for inventory control

---

## 🛠️ How It Works

1. **Data Preprocessing**  
   Historical consumption data is grouped weekly by Bar and Brand.

2. **Demand Forecasting**  
   Next week’s demand is predicted using the last 4 weeks’ average consumption.

3. **Par Level Calculation**  
   A safety buffer is added based on v
---

## 📷 Screenshots

| Forecasting & Summary Cards | Weekly Usage Trend |
|----------------------------|---------------------|
| ![metrics](./screenshots/metrics.png) | ![plot](./screenshots/plot.png) |

> *(Optional: add actual screenshots to `/screenshots` folder in GitHub)*

---

## 📈 Example Use Case

A bar manager selects their location and a specific alcohol brand in the dashboard. They instantly see:
- How much to stock next week
- The % risk of running out
- Estimated waste if demand is lower than expected
- A visual trend of weekly demand with the forecasted par level

---

## ✅ Future Improvements

- Add support for seasonality/event-based spikes
- Use advanced models (e.g., Prophet, LSTM) for long-term forecasting
- Real-time alerts for low inventory risk
- Direct POS system integration

---

## 🧠 Author

Built by [Your Name] – Final Year IT Student @ VIT Vellore  
📬 Contact: [your email] (optional)

---

## 📄 License

MIT License
ariability in demand using a z-score of 1.65 (95% confidence).

4. **Simulation**  
   Inventory performance is simulated week-by-week to show stockouts and overstock scenarios.

---

## 📁 Project Structure

├── app.py # Streamlit app script
├── requirements.txt # Python dependencies for deployment
├── filtered_weekly.csv # Weekly usage per bar-brand
├── par_level_recommendations.csv # Forecast + safety stock
├── inventory_simulation_results.csv # Simulation output


