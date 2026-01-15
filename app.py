import streamlit as st
import matplotlib.pyplot as plt
import calendar
import datetime
import matplotlib as mpl

# =========================
# 1. 한글 폰트 설정 (오류 없는 방식)
# =========================
mpl.rcParams["font.family"] = "DejaVu Sans"
mpl.rcParams["axes.unicode_minus"] = False

# =========================
# 2. 기본 설정
# =========================
st.set_page_config(page_title="울산 학교 일정 달력", layout="centered")
st.title("📅 울산 학교 일정 달력")

calendar.setfirstweekday(calendar.MONDAY)

# =========================
# 3. 일정 데이터
# =========================
events = {
    "2026-01-01": "신정",
    "2026-03-02": "1학기 개학",
    "2026-04-10": "중간고사",
    "2026-05-05": "어린이날",
    "2026-06-25": "기말고사",
    "2026-07-20": "여름방학",
    "2026-09-01": "2학기 개학",
    "2026-10-15": "체육대회",
    "2026-11-20": "수능",
    "2026-12-24": "겨울방학"
}

# =========================
# 4. 월 선택
# =========================
year = st.selectbox("연도 선택", [2026])
month = st.selectbox("월 선택", list(range(1, 13)))

# =========================
# 5. 달력 그리기
# =========================
cal = calendar.monthcalendar(year, month)

fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")

table = ax.table(
    cellText=cal,
    colLabels=["월", "화", "수", "목", "금", "토", "일"],
    loc="center",
    cellLoc="center"
)

table.scale(1, 2)

# =========================
# 6. 일정 있는 날짜 색칠
# =========================
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_facecolor("#DDDDDD")
        continue

    day = cell.get_text().get_text()
    if day.isdigit():
        date_str = f"{year}-{month:02d}-{int(day):02d}"
        if date_str in events:
            cell.set_facecolor("#FFCCCC")

# =========================
# 7. 출력
# =========================
st.pyplot(fig)

st.subheader("📌 이번 달 일정")
for date, event in events.items():
    y, m, d = date.split("-")
    if int(y) == year and int(m) == month:
        st.write(f"• {d}일 : {event}")
