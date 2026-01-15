import streamlit as st
import calendar
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(layout="wide")
calendar.setfirstweekday(calendar.MONDAY)

# ---------------------------
# 울산공업고등학교 일정 (예시)
# ---------------------------
EVENTS = {
    "2026-3-2": "입학식 · 개학",
    "2026-3-25": "전국연합학력평가",
    "2026-4-10": "중간고사",
    "2026-5-5": "어린이날",
    "2026-5-15": "학교 축제",
    "2026-6-20": "기말고사",
    "2026-7-20": "여름방학",
}

# ---------------------------
# 제목
# ---------------------------
st.title("📅 울산공업고등학교 일정 달력")

# ---------------------------
# 연/월 선택
# ---------------------------
year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 3)

# ---------------------------
# 달력 생성
# ---------------------------
cal = calendar.monthcalendar(year, month)

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 7)
ax.set_ylim(0, len(cal) + 1)
ax.axis("off")

# 요일 표시
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
for i, day in enumerate(weekdays):
    ax.text(i + 0.5, len(cal) + 0.5, day, ha="center", va="center", fontsize=16, fontweight="bold")

# 날짜 & 일정 표시
for week_idx, week in enumerate(cal):
    for day_idx, day in enumerate(week):
        if day == 0:
            continue

        y = len(cal) - week_idx - 0.5
        x = day_idx + 0.1

        date_key = f"{year}-{month}-{day}"
        event = EVENTS.get(date_key)

        # 일정 있는 날 배경색
        if event:
            ax.add_patch(plt.Rectangle((day_idx, y - 0.5), 1, 1, color="#FFD966"))

        # 날짜
        ax.text(x, y + 0.2, f"{day}", fontsize=16, fontweight="bold")

        # 일정 텍스트
        if event:
            ax.text(x, y - 0.1, event, fontsize=12, wrap=True)

# ---------------------------
# 출력
# ---------------------------
st.pyplot(fig)
