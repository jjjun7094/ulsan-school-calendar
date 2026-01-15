import os
import calendar
import datetime
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# =========================
# 🔹 한글 폰트 자동 설치
# =========================
FONT_PATH = "/tmp/NanumGothic.ttf"

if not os.path.exists(FONT_PATH):
    import urllib.request
    url = "https://github.com/naver/nanumfont/raw/master/fonts/NanumGothic.ttf"
    urllib.request.urlretrieve(url, FONT_PATH)

font_name = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False

# =========================
# 🔹 기본 설정
# =========================
calendar.setfirstweekday(calendar.MONDAY)
st.set_page_config(page_title="울산공업고 학사 달력", layout="wide")
st.title("📅 2026년 울산공업고등학교 학사 달력")

# =========================
# 🔹 학사 일정 (예시 – 필요시 추가 가능)
# =========================
events = {
    "2026-01-01": ("신정", "#FFE4E1"),
    "2026-02-27": ("입학식", "#FFF2CC"),
    "2026-03-02": ("1학기 개학", "#D9EAD3"),
    "2026-04-20": ("1학기 중간고사", "#F4CCCC"),
    "2026-05-21": ("체육대회", "#D0E0E3"),
    "2026-06-15": ("1학기 기말고사", "#F4CCCC"),
    "2026-06-25": ("여름방학 시작", "#EAD1DC"),
    "2026-08-17": ("2학기 개학", "#D9EAD3"),
    "2026-10-19": ("2학기 중간고사", "#F4CCCC"),
    "2026-11-03": ("학교 축제", "#D9D2E9"),
    "2026-12-07": ("2학기 기말고사", "#F4CCCC"),
    "2026-12-23": ("겨울방학", "#EAD1DC"),
}

# =========================
# 🔹 달력 그리기 함수
# =========================
def draw_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")

    table_data = [["월", "화", "수", "목", "금", "토", "일"]]

    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                key = f"{year}-{month:02d}-{day:02d}"
                if key in events:
                    row.append(f"{day}\n{events[key][0]}")
                else:
                    row.append(str(day))
        table_data.append(row)

    table = ax.table(cellText=table_data, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1.2, 2.2)

    # 주말 색상
    for r in range(1, len(table_data)):
        table[r, 5].set_facecolor("#E3F2FD")  # 토요일
        table[r, 6].set_facecolor("#FCE4EC")  # 일요일

    # 일정 있는 날 색상
    for r in range(1, len(table_data)):
        for c in range(7):
            text = table_data[r][c]
            if "\n" in text:
                day = text.split("\n")[0]
                key = f"{year}-{month:02d}-{int(day):02d}"
                table[r, c].set_facecolor(events[key][1])

    ax.set_title(f"{year}년 {month}월 학사 달력", fontsize=20, pad=20)
    st.pyplot(fig)

# =========================
# 🔹 월 이동 컨트롤
# =========================
if "current_month" not in st.session_state:
    st.session_state.current_month = 1

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("◀ 이전 달"):
        st.session_state.current_month -= 1
        if st.session_state.current_month < 1:
            st.session_state.current_month = 12

with col3:
    if st.button("다음 달 ▶"):
        st.session_state.current_month += 1
        if st.session_state.current_month > 12:
            st.session_state.current_month = 1

draw_calendar(2026, st.session_state.current_month)
