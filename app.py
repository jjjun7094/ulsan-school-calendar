import streamlit as st
import calendar

st.set_page_config(layout="wide")

# =====================
# 월 상태 저장 (핵심)
# =====================
if "year" not in st.session_state:
    st.session_state.year = 2026
if "month" not in st.session_state:
    st.session_state.month = 5

YEAR = st.session_state.year
MONTH = st.session_state.month

# =====================
# 일정 (한국어)
# =====================
events = {
    (2026, 5, 5): "어린이날",
    (2026, 5, 21): "체육대회"
}

# 요일
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

# =====================
# 월 이동 버튼
# =====================
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("◀ 이전 달"):
        if MONTH == 1:
            st.session_state.month = 12
            st.session_state.year -= 1
        else:
            st.session_state.month -= 1
        st.rerun()

with col3:
    if st.button("다음 달 ▶"):
        if MONTH == 12:
            st.session_state.month = 1
            st.session_state.year += 1
        else:
            st.session_state.month += 1
        st.rerun()

# =====================
# CSS (가독성)
# =====================
st.markdown("""
<style>
.calendar {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
}

.calendar th {
    padding: 12px;
    border: 1px solid #444;
    font-size: 18px;
    color: white;
    background-color: #1f2937;
}

.calendar td {
    height: 120px;
    vertical-align: top;
    padding: 10px;
    border: 1px solid #333;
    color: white;
    font-size: 16px;
}

.day {
    font-size: 20px;
    font-weight: bold;
}

.event {
    background-color: rgba(46, 204, 113, 0.25);
    border-left: 5px solid #2ecc71;
}

.event-text {
    margin-top: 8px;
    font-size: 14px;
    color: white;
}

.sat {
    background-color: rgba(52, 152, 219, 0.2);
}

.sun {
    background-color: rgba(231, 76, 60, 0.2);
}
</style>
""", unsafe_allow_html=True)

# =====================
# 제목
# =====================
st.markdown(
    f"<h1 style='text-align:center;'>{YEAR}년 {MONTH}월</h1>",
    unsafe_allow_html=True
)

# =====================
# 달력 생성
# =====================
cal = calendar.Calendar(firstweekday=0)
month_days = cal.monthdayscalendar(YEAR, MONTH)

html = "<table class='calendar'>"

# 요일
html += "<tr>"
for wd in weekdays:
    html += f"<th>{wd}</th>"
html += "</tr>"

# 날짜
for week in month_days:
    html += "<tr>"
    for i, day in enumerate(week):
        classes = []

        if i == 5:
            classes.append("sat")
        if i == 6:
            classes.append("sun")
        if (YEAR, MONTH, day) in events:
            classes.append("event")

        class_str = " ".join(classes)

        if day == 0:
            html += "<td></td>"
        else:
            html += f"<td class='{class_str}'>"
            html += f"<div class='day'>{day}</div>"
            if (YEAR, MONTH, day) in events:
                html += f"<div class='event-text'>{events[(YEAR, MONTH, day)]}</div>"
            html += "</td>"
    html += "</tr>"

html += "</table>"

st.markdown(html, unsafe_allow_html=True)
