import streamlit as st
import calendar
import matplotlib.pyplot as plt
from datetime import date

# ===============================
# 기본 설정
# ===============================
st.set_page_config(page_title="울산공업고등학교 일정 달력", layout="wide")

calendar.setfirstweekday(calendar.MONDAY)

# ===============================
# 일정 데이터 (예시)
# ===============================
events = {
    "2026-5-5": "어린이날",
    "2026-5-21": "중간고사",
    "2026-5-28": "체육대회",
}

# ===============================
# 제목
# ===============================
st.title("📅 울산공업고등학교 일정 달력")

# ===============================
# 연 / 월 선택
# ===============================
year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 5)

# ===============================
# 요일 (한국어)
# ===============================
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

# ===============================
# 달력 데이터
# ===============================
cal = calendar.monthcalendar(year, month)

# ===============================
# 그래프 크기 조절 (너무 크지 않게)
# ===============================
fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 7)
ax.set_ylim(0, len(cal) + 1)
ax.axis("off")

# ===============================
# 요일 헤더
# ===============================
for i, day in enumerate(weekdays):
    ax.text(i + 0.5, len(cal) + 0.5, day, ha="center", va="center", fontsize=13, weight="bold")

# ===============================
# 달력 그리기
# ===============================
for row, week in enumerate(cal):
    y = len(cal) - row - 1
    for col, day in enumerate(week):
        if day == 0:
            ax.add_patch(plt.Rectangle((col, y), 1, 1, fill=False))
            continue

        date_key = f"{year}-{month}-{day}"

        # 기본 색
        color = "white"

        # 일정 있는 날
        if date_key in events:
            color = "#FFF3B0"

        # 토요일 / 일요일 색
        if col == 5:
            color = "#EAF2FF"
        if col == 6:
            color = "#FFECEC"

        ax.add_patch(plt.Rectangle((col, y), 1, 1, facecolor=color, edgecolor="black"))

        # 날짜 숫자
        ax.text(col + 0.05, y + 0.75, str(day), ha="left", va="center", fontsize=12, weight="bold")

        # 일정 텍스트
        if date_key in events:
            ax.text(
                col + 0.05,
                y + 0.4,
                events[date_key],
                ha="left",
                va="top",
                fontsize=10,
            )

# ===============================
# 출력
# ===============================
st.pyplot(fig)
