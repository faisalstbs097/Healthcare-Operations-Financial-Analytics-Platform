
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Operations & Financial Analytics Platform",
    page_icon="🏥",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================

page = st.sidebar.radio(
    "Navigation",
    [
        "🏥 Project Overview",
        "📂 Data Model",
        "📋 Data Quality Findings",
        "⚙ SQL Analytics",
        "🐍 Python Analytics",
        "📊 Interactive Analytics",
        "📊 Power BI Dashboard",
        "💡 Business Insights",
        "🎯 Recommendations",
        "🔗 Resources",
        "👨‍💻 About Developer"
    ]
)

# =========================
# OVERVIEW
# =========================

if page == "🏥 Project Overview":

    st.title("🏥 Healthcare Operations & Financial Analytics Platform")

    st.markdown("""
    ### End-to-End Healthcare Analytics using SQL, Python (Pandas), Power BI and DAX
    """)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Patients", "326K")
    col2.metric("Total Visits", "905K")
    col3.metric("Revenue", "₹903.41 Cr")
    col4.metric("Average Bill", "₹9.85K")

    st.divider()

    st.header("Project Objective")

    st.write("""
    Analyze healthcare operations and financial performance using
    Patient, Visit, Diagnosis, Treatment and Billing datasets.

    The project combines SQL, Python (Pandas), Power BI and DAX
    to generate actionable business insights.
    """)

    st.subheader("Technology Stack")

    st.markdown("""
    - SQL
    - Python (Pandas)
    - Power BI
    - DAX
    - Excel
    - Streamlit
    """)

# =========================
# DATA MODEL
# =========================

elif page == "📂 Data Model":

    st.title("📂 Healthcare Data Model")

    st.code("""
PATN
│
├── PAT_ID
│
▼
VIST
│
├── PAT_ID
├── REFR_NO
│
▼
DIAG
│
├── REFR_NO
│
▼
TRTM
│
├── REFR_NO
│
▼
BILL
""")

    st.markdown("""
### Relationship Discovery

**PATN → VIST**

- One Patient can have Multiple Visits

**VIST → DIAG**

- One Visit can have Multiple Diagnoses

**VIST → TRTM**

- One Visit can have Multiple Treatments

**VIST → BILL**

- Billing linked through REFR_NO
""")

# =========================
# DATA QUALITY
# =========================

elif page == "📋 Data Quality Findings":

    st.title("📋 Data Quality Findings")

    st.markdown("""
### Patient Table Findings

✅ DOB column contained mixed formats

Examples:

- 6/18/2000
- 05-09-2012
- 06-10-1991

### Invalid Dates Found

- 10-02-0035
- 00-03-2008

### Missing Values

- Middle Name fields contained NULL values

### Validation Issues

- Future date validation required

### Dataset Observation

- Gender distribution appears synthetically balanced
- Diagnosis and treatment visits are nearly identical
""")

# =========================
# SQL ANALYTICS
# =========================

elif page == "⚙ SQL Analytics":

    st.title("⚙ SQL Analytics")

    st.success("26+ SQL Queries Implemented")

    st.subheader("Revenue By Visit Type")

    st.code("""
SELECT v.vtype_des,
       SUM(b.bill_amt) AS revenue
FROM billing b
JOIN vist v
ON b.refr_no = v.refr_no
GROUP BY v.vtype_des
ORDER BY revenue DESC;
""", language="sql")

    st.subheader("Top Revenue Generating Patients (CTE)")

    st.code("""
WITH patient_revenue AS
(
SELECT pat_id,
SUM(bill_amt) AS revenue
FROM billing
GROUP BY pat_id
)
SELECT *
FROM patient_revenue
ORDER BY revenue DESC
LIMIT 5;
""", language="sql")

    st.subheader("Patient Revenue Ranking")

    st.code("""
SELECT pat_id,
SUM(bill_amt) AS revenue,
RANK() OVER
(
ORDER BY SUM(bill_amt) DESC
) AS revenue_rank
FROM billing
GROUP BY pat_id;
""", language="sql")

    st.subheader("Monthly Revenue Trend")

    st.code("""
SELECT MONTH(bill_date) AS month_no,
SUM(bill_amt) AS revenue
FROM billing
GROUP BY MONTH(bill_date)
ORDER BY month_no;
""", language="sql")
    
    st.info("Additional SQL queries covering subqueries, ranking, LAG, LEAD, running totals, and advanced aggregations are available in the GitHub repository.")

# =========================
# PYTHON ANALYTICS
# =========================

elif page == "🐍 Python Analytics":

    st.title("🐍 Python Analytics")

    st.success("Data Cleaning • EDA • Feature Engineering")

    st.subheader("Column Standardization")

    st.code("""
df_patn.columns = (
df_patn.columns
.str.strip()
.str.lower()
)
""", language="python")

    st.subheader("Duplicate Analysis")

    st.code("""
df_patn['pat_id']
.duplicated()
.sum()
""", language="python")

    st.subheader("Date Conversion")

    st.code("""
df_patn['dt_brt']=pd.to_datetime(
df_patn['dt_brt'],
errors='coerce'
)
""", language="python")

    st.subheader("Age Engineering")

    st.code("""
df_patn['age'] =
(
(today-df_patn['dt_brt'])
.dt.days // 365
)
""", language="python")

    st.subheader("Age Group Creation")

    st.code("""
df_patn['age_group']=pd.cut(
df_patn['age'],
bins=[0,18,30,45,60,120]
)
""", language="python")

    st.subheader("Merge Operation")

    st.code("""
diag_merge = pd.merge(
df_diag1,
df_vist,
on='refr_no',
how='inner'
)
""", language="python")

    st.subheader("Treatment Trend Analysis")

    st.code("""
df_treatment.groupby(
df_treatment['trtm_en'].dt.month
)['refr_no'].count()
""", language="python")

# =========================
# INTERACTIVE ANALYTICS
# =========================

elif page == "📊 Interactive Analytics":

    st.title("📊 Interactive Analytics")

    metrics = pd.DataFrame({
        "Metric":
        ["Patients","Visits","Revenue(Cr)","Avg Bill(K)"],
        "Value":
        [326,905,903.41,9.85]
    })

    st.subheader("Healthcare KPI Comparison")
    st.bar_chart(metrics.set_index("Metric"))

    data_df = pd.DataFrame({
        "Dataset":
        ["Patients","Visits","Diagnosis","Treatments"],
        "Records":
        [326000,905000,950000,900000]
    })

    st.subheader("Dataset Volume")
    st.bar_chart(data_df.set_index("Dataset"))

    skill_df = pd.DataFrame({
        "Technology":
        ["SQL","Python","Power BI","Excel"],
        "Coverage":
        [40,30,20,10]
    })

    st.subheader("Project Skill Distribution")
    st.bar_chart(skill_df.set_index("Technology"))

# =========================
# DASHBOARD
# =========================

elif page == "📊 Power BI Dashboard":

    st.title("📊 Power BI Dashboard")

    st.image(
        "Dashboard_image.png",
        use_container_width=True
    )

# =========================
# INSIGHTS
# =========================

elif page == "💡 Business Insights":

    st.title("💡 Business Insights")

    st.markdown("""
### Patient Utilization

- Total Patients exceeded 326K
- Healthcare Visits exceeded 905K
- Average Visits Per Patient ≈ 2.82

### Financial Performance

- Revenue exceeded ₹903.41 Cr
- Average Bill Amount = ₹9.85K

### Diagnosis Analysis

- 39 Diagnosis Categories identified
- High-volume diagnosis groups analyzed

### Treatment Analysis

- Treatment Mix Analysis performed
- Broad treatment distribution observed
""")

# =========================
# RECOMMENDATIONS
# =========================

elif page == "🎯 Recommendations":

    st.title("🎯 Business Recommendations")

    st.markdown("""
1. Monitor repeat patients with more than 5 visits.

2. Track high-revenue patient segments.

3. Improve diagnosis quality monitoring.

4. Build treatment outcome reporting.

5. Develop predictive revenue forecasting.

6. Strengthen patient retention analytics.
""")

# =========================
# RESOURCES
# =========================

elif page == "🔗 Resources":

    st.title("🔗 Project Resources")

    st.link_button(
        "📂 GitHub Repository",
        "https://github.com/faisalstbs097/Healthcare-Operations-Financial-Analytics-Platform"
    )

    st.link_button(
        "📄 PDF Presentation",
        "https://github.com/faisalstbs097/Healthcare-Operations-Financial-Analytics-Platform/blob/main/Healthcare-PDF.pdf"
    )

    st.info(
        "Power BI Dashboard, SQL Scripts, Python Notebook and Documentation are available in the GitHub repository."
    )

# =========================
# ABOUT DEVELOPER
# =========================

elif page == "👨‍💻 About Developer":

    st.title("👨‍💻 About Developer")

    st.markdown("""
### Faisal Ahmed

**B.Tech – Computer Science & Engineering**

Meghnad Saha Institute of Technology

Batch: 2022 – 2026

Aspiring Data Analyst | Business Intelligence Analyst

### Skills

- SQL
- Python
- Pandas
- Power BI
- Excel
- Streamlit
""")

    st.success(
        "Built Healthcare Operations & Financial Analytics Platform as an end-to-end analytics project."
    )