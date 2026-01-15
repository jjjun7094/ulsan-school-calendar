import streamlit as st
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import matplotlib as mpl
import datetime
import os

# =========================
# 한글 폰트 설정 (핵심)
# =========================
font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
if os.path.exists(font_path):
    font_prop = fm.FontProperties(fname=font_path)
    mpl.rcParams["font.family"] = font_prop.get_name()
else:
    mpl.rcParams["font.family"] = "DejaVu Sans"
mpl.rcParams["axes.unicode_minus"] = False

# =========================
# Streamlit 기본 설정
# =========================
st.set_page_config(page_title="울산공업고등학교 일정 달력", layout="wide")
st.title("📅 울산공업고등학교 일정 달력")

# =========================
# 일정 데이터 (예시)
# =========================
events = {
    "2026-05-05": "어린이날",
    "2026-05-21": "체육대회",
    "2026-05-27": "중간고사",
}

# =========================
# 연도 / 월 선택
# =========================
year = st.selectbox("연도 선택", [2025, 2026, 2027], index=1)
month = st.slider("월 선택", 1, 12, 5)

# =========================
# 달력 데이터 생성
# =========================
cal = calendar.Calendar(firstweekday=0)  # 월요일 시작
month_days = cal.monthdayscalendar(year, month)

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

# =========================
# 달력 그리기
# =========================
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_xlim(0, 7)
ax.set_ylim(0, len(month_days))
ax.axis("off")

# 요일 제목
for i, day in enumerate(weekdays):
    ax.text(i + 0.5, len(month_days) + 0.2, day,
            ha="center", va="bottom", fontsize=14, weight="bold")

# 날짜 칸
for row, week in enumerate(month_days):
    for col, day in enumerate(week):
        if day == 0:
            continue

        y = len(month_days) - row - 1
        date_str = f"{year}-{month:02d}-{day:02d}"

        # 기본 색
        facecolor = "white"

        # 토요일 / 일요일 색
        if col == 5:
            facecolor = "#E8F1FF"
        if col == 6:
            facecolor = "#FFECEC"

        # 일정 있는 날 색
        if date_str in events:
            facecolor = "#FFF3B0"

        rect = patches.Rectangle((col, y), 1, 1,
                                 linewidth=1, edgecolor="black",
                                 facecolor=facecolor)
        ax.add_patch(rect)

        # 날짜 숫자
        ax.text(col + 0.05, y + 0.9, str(day),
                ha="left", va="top", fontsize=13, weight="bold")

        # 일정 텍스트
        if date_str in events:
            ax.text(col + 0.05, y + 0.6, events[date_str],
                    ha="left", va="top", fontsize=11)

# 월 제목
ax.text(3.5, len(month_days) + 0.8,
        f"{year}년 {month}월",
        ha="
