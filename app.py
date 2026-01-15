import streamlit as st
import calendar
from datetime import date

st.set_page_config(page_title="울산공업고등학교 일정 달력", layout="wide")
calendar.setfirstweekday(calendar.MONDAY)

# ---------------------------
# 일정 (한국어)
# ---------------------------
events = {
    "2026-05-05": "어린이날",
    "2026-05-21": "체육대회",
}

# ---------------------------
# 제목 / 선택
# ---------------------------
st.title("🏫 울산공업고등학교 일정 달력")

year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 5)

# ---------------------------
# 요일
# ---------------------------
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
cols = st.columns(7)
for c, d in zip(cols, weekdays):
    c.markdown(f"**{d}**")

st.markdown("---")

# ---------------------------
# 달력 생성 (HTML)
# ---------------------------
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
  vertical-align: top;
  padding: 6px;
}
.sat { background-color: #e8f1ff; }
.sun { background-color: #ffecec; }
.event { background-color: #fff3b0; }
.day { font-weight: bold; }
.event-text { font-size: 13px; margin-top: 4px; }
</style>
<table class="calendar">
"""

for week in cal:
    html += "<tr>"
    for i, day in enumerate(week):
        cls = ""
        if i == 5:
            cls = "sat"
        if i == 6:
            cls = "sun"

        if day == 0:
            html += "<td></td>"
        else:
            key = f"{year}-{month:02d}-{day:02d}"
            if key in events:
                cls += " event"
                html += f"""
                <td class="{cls}">
                  <div class="day">{day}</div>
                  <div class="event-text">{events[key]}</div>
                </td>
                """
            else:
                html += f"<td class='{cls}'><div class='day'>{day}</div></td>"
    html += "</tr>"

html += "</table>"

st.markdown(f"<h2 style='text-align:center'>{year}년 {month}월</h2>", unsafe_allow_html=True)
st.markdown(html, unsafe_allow_html=True)
