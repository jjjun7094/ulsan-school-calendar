import streamlit as st
import calendar

# =========================
# 기본 설정
# =========================
st.set_page_config(
    page_title="울산공업고등학교 일정 달력",
    layout="wide"
)

calendar.setfirstweekday(calendar.MONDAY)

# =========================
# 학사 일정 (한국어)
# =========================
events = {
    "2026-5-5": "어린이날",
    "2026-5-21": "체육대회",
    "2026-4-10": "중간고사",
    "2026-6-10": "기말고사",
}

# =========================
# 제목 & 선택
# =========================
st.title("🏫 울산공업고등학교 일정 달력")

year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 5)

# =========================
# 요일 (한국어)
# =========================
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
cols = st.columns(7)

for col, day in zip(cols, weekdays):
    col.markdown(
        f"<div style='text-align:center; font-weight:bold; font-size:18px; color:white;'>{day}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# =========================
# 달력 HTML 생성
# =========================
cal = calendar.monthcalendar(year, month)

html = """
<style>
.calendar {
    width: 100%;
    border-collapse: collapse;
}
.calendar td {
    border: 1px solid #444;
    height: 90px;
    padding: 6px;
    vertical-align: top;
    color: white;
    font-size: 16px;
}
.day {
    font-weight: bold;
}
.event {
    background-color: #c8f7c5;
    color: black;
}
.event .day {
    color: black;
}
.event-text {
    font-size: 13px;
    margin-top: 4px;
}
.sat {
    background-color: #1e3a5f;
}
.sun {
    background-color: #5f1e1e;
}
</style>

<h2 style="text-align:center;">{year}년 {month}월</h2>
<table class="calendar">
"""

for week in cal:
    html += "<tr>"
    for i, day in enumerate(week):
        if day == 0:
            html += "<td></td>"
        else:
            key = f"{year}-{month}-{day}"
            cls = ""
            if i == 5:
                cls = "sat"
            if i == 6:
                cls = "sun"

            if key in events:
                html += f"""
                <td class="event {cls}">
                    <div class="day">{day}</div>
                    <div class="event-text">{events[key]}</div>
                </td>
                """
            else:
                html += f"""
                <td class="{cls}">
                    <div class="day">{day}</div>
                </td>
                """
    html += "</tr>"

html += "</table>"

st.markdown(html, unsafe_allow_html=True)
