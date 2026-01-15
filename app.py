import streamlit as st
import matplotlib.pyplot as plt
import calendar
from matplotlib import font_manager
import matplotlib as mpl
import os

# 한글 폰트 설정
font_path = "./NanumGothic.ttf"
if os.path.exists(font_path):
    font_manager.fontManager.addfont(font_path)
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    mpl.rcParams["font.family"] = font_name
mpl.rcParams["axes.unicode_minus"] = False

calendar.setfirstweekday(calendar.MONDAY)

events = {
    "2026-01-01": "신정",
    "2026-03-02": "1학기 개학/입학식",
    "2026-04-10": "중간고사",
    "2026-05-05": "어린이날",
    "2026-05-21": "체육대회",
    "2026-06-10": "기말고사",
    "2026-06-23": "여름방학",
    "2026-09-01": "2학기 개학",
    "2026-10-20": "중간고사",
    "2026-12-08": "기말고사",
    "2026-12-23": "겨울방학"
}

def draw_month(year, month):
    cal = calendar.monthcalendar(year, month)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis("off")

    table_data = [["월","화","수","목","금","토","일"]]
    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                key = f"{year}-{month:02d}-{day:02d}"
                row.append(f"{day}\n{events[key]}" if key in events else str(day))
        table_data.append(row)

    table = ax.table(cellText=table_data, cellLoc="center", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 1.8)

    for r in range(1, len(table_data)):
        table[r,5].set_facecolor("#DDEBFF")
        table[r,6].set_facecolor("#FFD6D6")

    ax.set_title(f"2026년 {month}월 울산공업고 학사 달력", fontsize=15)
    st.pyplot(fig)

st.set_page_config(page_title="울산공업고 학사 달력")
st.title("📅 2026년 울산공업고 학사 달력")

month = st.selectbox("월 선택", list(range(1, 13)))
draw_month(2026, month)
