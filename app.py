import streamlit as st
import calendar
from datetime import date

st.set_page_config(layout="wide")

# =====================
# 설정
# =====================
YEAR = 2026
MONTH = 5

# 일정 (한국어만)
events = {
    5: "어린이날",
    21: "체육대회"
}

# 요일 (월~일)
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

# =====================
# CSS (가독성 해결 핵심)
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
    background-color: rgba(46, 204, 113, 0.25); /* 연한 초록 */
    border-left: 5px solid #2ecc71;
}

.event-text {
    margin-top: 8px;
    font-size: 14px;
    color: #ffffff;  /* 일정 글자 흰색 */
}

/* 토요일 */
.sat {
    background-color: rgba(52, 152, 219, 0.2);
}

/* 일요일 */
.sun {
    background-color: rgba(231, 76, 60, 0.2);
}
</style>
""", unsafe_allow_html=True)

# =====================
# 제목
# =====================
st.markdown(f"<h1 style='text-align:center;'>{YEAR}년 {MONTH}월</h1>", unsafe_allow_html=True)

# =====================
# 달력 생성
# =====================
cal = calendar.Calendar(firstweekday=0)  # 월요일 시작
month_days = cal.monthdayscalendar(YEAR, MONTH)

html = "<table class='calendar'>"

# 요일 헤더
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
        if day in events:
            classes.append("event")

        class_str = " ".join(classes)

        if day == 0:
            html += "<td></td>"
        else:
            html += f"<td class='{class_str}'>"
            html += f"<div class='day'>{day}</div>"
            if day in events:
                html += f"<div class='event-text'>{events[day]}</div>"
            html += "</td>"
    html += "</tr>"

html += "</table>"

st.markdown(html, unsafe_allow_html=True)
