import streamlit as st
from streamlit_option_menu import option_menu
from stock_utils import (
    load_data, clean_data, plot_close_hist, plot_volume_pie, 
    plot_box_close, plot_regression_close_volume, plot_line_ohlc,
    plot_close_with_normal_curve, calculate_close_statistics,
    calculate_confidence_interval, plot_bar_chart
)

st.set_page_config(page_title="Stock Exchange Analysis Report", layout="wide")

# Apply custom CSS
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# st.markdown(
#     """
#     <div style='background-color:#021526;padding:28px;border-radius:10px;margin-bottom:20px;position:relative;'>
#         <img src='https://raw.githubusercontent.com/Steelman9876/logo/main/a-logo-with-the-text-squardon-x-in-a-mod_wdxq7gxLRuiZhutKtct7Vg_yEPFiJ02T7m6OMAVyelz6A.jpeg' width='120' height='120' style='border-radius:50%;position:absolute;left:20px;top:50%;transform:translateY(-50%);' />
#         <h1 style='color:#E2E2B6;text-align:center;margin:0;font-size:40px;'>SQUADRON X</h1>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


st.markdown(
    """
    <div style='
       background: linear-gradient(90deg, #0B3D0B 0%, #4CAF50 100%);
        padding:28px;
        border-radius:10px;
        margin-bottom:20px;
        position:relative;
    '>
        <img src='https://raw.githubusercontent.com/Steelman9876/logo/main/a-logo-with-the-text-squardon-x-in-a-mod_wdxq7gxLRuiZhutKtct7Vg_yEPFiJ02T7m6OMAVyelz6A.jpeg'
             width='120' height='120'
             style='border-radius:50%;position:absolute;left:20px;top:50%;transform:translateY(-50%);' />
        <h1 style='color:#E2E2B6;text-align:center;margin:0;font-size:32px;'>Pakistan Stock Exchange Analysis</h1>
        <h1 style='color:#E2E2B6;text-align:center;margin:0;font-size:32px;'>by SQUADRON X</h1>
  
    </div>
    """,
    unsafe_allow_html=True
)


# Horizontal Navigation
selected = option_menu(
    menu_title=None,
    options=["Overview", "Visualizations", "Contact"],
    icons=["bar-chart-line", "graph-up", "envelope"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "#6EACDA", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "color": "#021526"},
        "nav-link-selected": {"background-color": "#03346E", "color": "white"},
    }
)


# Load once to reuse
data = clean_data(load_data())

# Page Logic
if selected == "Overview":
    # Header
    st.markdown("## 🎯 Dashboard Overview")
    st.markdown("Comprehensive analysis of Pakistan Stock Exchange (KSE-100) performance between **2015–2021**.")

    # Key Metrics in Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style='background-color:white;padding:20px;border-radius:10px;border:2px solid #03346E;text-align:center;'>
                <h3 style='color:#03346E;margin:0;'>📊 Data Points</h3>
                <p style='color:#021526;font-size:24px;margin:10px 0;'><strong>1500+</strong></p>
                <p style='color:#6EACDA;margin:0;'>Daily Market Entries</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color:white;padding:20px;border-radius:10px;border:2px solid #03346E;text-align:center;'>
                <h3 style='color:#03346E;margin:0;'>🕒 Time Span</h3>
                <p style='color:#021526;font-size:24px;margin:10px 0;'><strong>7 Years</strong></p>
                <p style='color:#6EACDA;margin:0;'>Historical Data</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background-color:white;padding:20px;border-radius:10px;border:2px solid #03346E;text-align:center;'>
                <h3 style='color:#03346E;margin:0;'>📈 Index Coverage</h3>
                <p style='color:#021526;font-size:24px;margin:10px 0;'><strong>KSE-100</strong></p>
                <p style='color:#6EACDA;margin:0;'>Market Benchmark</p>
            </div>
        """, unsafe_allow_html=True)

    # Feature Highlights
    st.markdown("### 🌟 Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background-color:#f0f2f6;padding:20px;border-radius:10px;margin:10px 0;'>
            <h4 style='color:#03346E;margin:0 0 10px 0;'>📊 Analysis Tools</h4>
            <ul style='color:#021526;margin:0;padding-left:20px;'>
                <li>Interactive Visualizations</li>
                <li>Statistical Analysis</li>
                <li>Trend Detection</li>
                <li>Price Movement Patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style='background-color:#f0f2f6;padding:20px;border-radius:10px;margin:10px 0;'>
            <h4 style='color:#03346E;margin:0 0 10px 0;'>📈 Market Indicators</h4>
            <ul style='color:#021526;margin:0;padding-left:20px;'>
                <li>Daily Price Movements</li>
                <li>Volume Analysis</li>
                <li>Market Trends</li>
                <li>Historical Patterns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Data Preview Section
    st.markdown("### 📋 Quick Data Preview")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.dataframe(data.head(5), use_container_width=True)
    with col2:
       st.markdown("""
        <div style='background-color:#021526;padding:20px;border-radius:10px;text-align:center;'>
            <h4 style='color:#E2E2B6;margin:0 0 10px 0;'>📥 Download Dataset</h4>
            <p style='color:white;font-size:14px;margin:0 0 20px 0;'>Get the complete KSE-100 dataset for your analysis</p>
            <a href='stock-exchange-kse-100pakistan.csv' download='KSE100_Data.xlsx'>
                <button style='
                    background-color:#0B4F8A;
                    color:white;
                    border:none;
                    padding:10px 20px;
                    border-radius:8px;
                    font-size:15px;
                    cursor:pointer;
                    width:100%;
                '
                onmouseover="this.style.backgroundColor='#1565C0'"
                onmouseout="this.style.backgroundColor='#0B4F8A'"
                >
                    📥 Download Dataset
                </button>
            </a>
        </div>
    """, unsafe_allow_html=True)
       
        # Center the download button
        # col_space1, col_btn, col_space2 = st.columns([0.1, 5, 0.001])
        # with col_btn:
        #     st.download_button(
        #         label="📥 Download Dataset",
        #         data=open("stock-exchange-kse-100pakistan.csv", "rb"),
        #         file_name="KSE100_Data.xlsx",
        #         mime="application/vnd.ms-excel",
        #         use_container_width=True  # Make button fill container width
        #     )

elif selected == "Visualizations":
    st.markdown("## 📈 Visualizations")
    viz_option = st.selectbox(
        "Select Visualization",
        ["Bar Chart", "Box-Whisker Plot", "Pie Chart", "Histogram", "Regression", 
         "Line Chart", "Normal Curve", "Statistics", "Confidence Interval"]
    )

    if viz_option == "Bar Chart":
        fig = plot_bar_chart(data)
        st.pyplot(fig)
        st.info("This chart displays the average closing price for each year in the dataset.")

    elif viz_option == "Box-Whisker Plot":
        fig = plot_box_close(data)
        st.pyplot(fig)

    elif viz_option == "Pie Chart":
        fig = plot_volume_pie(data)
        st.pyplot(fig)

    elif viz_option == "Histogram":
        fig = plot_close_hist(data)
        st.pyplot(fig)

    elif viz_option == "Regression":
        fig, coef, intercept = plot_regression_close_volume(data)
        st.pyplot(fig)
        st.success(f"Regression Coefficient: **{coef:.4f}**")
        st.success(f"Intercept: **{intercept:.2f}**")
    elif viz_option == "Line Chart":
        fig = plot_line_ohlc(data)
        st.pyplot(fig)

    elif viz_option == "Normal Curve":
        fig, mu, sigma = plot_close_with_normal_curve(data)
        st.pyplot(fig)
        st.info(f"Fitted Normal Distribution → **Mean** = `{mu:.2f}`, **Std Dev** = `{sigma:.2f}`")
    
    elif viz_option == "Statistics":
        stats_dict = calculate_close_statistics(data)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📊 Basic Statistics")
            st.success(f"📌 Mean: **{stats_dict['mean']}**")
            st.success(f"📌 Median: **{stats_dict['median']}**")
        
        with col2:
            st.markdown("### 📉 Dispersion Measures")
            st.success(f"📌 Variance: **{stats_dict['variance']}**")
            st.success(f"📌 Standard Deviation: **{stats_dict['std_dev']}**")
    
    elif viz_option == "Confidence Interval":
        n, mean, std_dev, lower_bound, upper_bound = calculate_confidence_interval(data)
        
        st.markdown("### 📊 Confidence Interval Analysis")
        st.info("95% Confidence Interval for Mean Closing Price")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"📈 Sample Size (n): **{n}**")
            st.success(f"📊 Mean Price: **{mean:.2f}**")
            st.success(f"📏 Std Deviation: **{std_dev:.2f}**")
        
        with col2:
            st.success(f"⬇️ Lower Bound: **{lower_bound:.2f}**")
            st.success(f"⬆️ Upper Bound: **{upper_bound:.2f}**")
        
        st.info("*We can be 95% confident that the true population mean falls within this interval.*")
    
elif selected == "Contact":
    st.markdown("## 📬 Meet Our Team")
    
    # Custom CSS for hover effects and cards
    st.markdown("""
        <style>
        .team-card {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            transition: all 0.3s ease;
            border: 2px solid #03346E;
        }
        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(3, 52, 110, 0.3);
            background-color: #03346E;
        }
        .team-card:hover p {
            color: white !important;
        }
        .team-card:hover .email {
            color: #6EACDA !important;
        }
        .header-section {
            background: linear-gradient(135deg, #021526, #03346E);
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Header Section
    st.markdown("""
        <div class='header-section'>
            <h2 style='color:#E2E2B6;margin:0;'>Squadron X Development Team</h2>
            <p style='color:#6EACDA;margin:10px 0 0;'>Building Pakistan's Premier Stock Analysis Platform</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Team Members in Interactive Cards
    col1, col2 = st.columns(2)
    
    with col1:
        team_members = [
            ("Syed Ayaan Hassan Shah", "f230711"),
            ("Muhammad Anwaar Ahmad", "f230540"),
            ("Muhammad Luqman Waseem", "f230640")
        ]
        for name, roll_no in team_members:
            st.markdown(f"""
                <div class='team-card'>
                    <p style='color:#03346E;font-size:20px;margin:0;'>👤 {name}</p>
                    <p class='email' style='color:#6EACDA;margin:10px 0;'>
                        📧 {roll_no.lower()}@cfd.nu.edu.pk
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        team_members = [
            ("Muhammad Mahroz Sarmad", "f230539"),
            ("Minahil Khan", "f230576")
        ]
        for name, roll_no in team_members:
            st.markdown(f"""
                <div class='team-card'>
                    <p style='color:#03346E;font-size:20px;margin:0;'>👤 {name}</p>
                    <p class='email' style='color:#6EACDA;margin:10px 0;'>
                        📧 {roll_no.lower()}@cfd.nu.edu.pk
                    </p>
                </div>
            """, unsafe_allow_html=True)
    
    # Footer Section
    st.markdown("""
        <div style='background: linear-gradient(135deg, #03346E, #021526);
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                    margin-top: 30px;'>
            <h3 style='color:#E2E2B6;margin:0 0 10px 0;'>📫 Connect With Us</h3>
            <p style='color:white;font-size:18px;margin:5px 0;'></p>
            <div style='margin-top:15px;padding-top:15px;border-top:1px solid #6EACDA;'>
                <p style='color:#6EACDA;font-size:14px;margin:0;'>
                    KSE-100 Analysis Project | Made with 💙 by Squadron X
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
