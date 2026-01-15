import streamlit as st
import calendar
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl

# ===============================
# 🔥 한글 폰트 설정 (이게 핵심)
# ===============================
font_path = fm.findfont(fm.FontProperties(family="NanumGothic"))
font_prop = fm.FontProperties(fname=font_path)
mpl.rcParams["font.family"] = font_prop.get_name()
mpl.rcParams["axes.unicode_minus"] = False

# ===============================
st.set_page_config(page_title="울산공업고등학교 일정 달력", layout="wide")
calendar.setfirstweekday(calendar.MONDAY)

# ===============================
# 일정 (한글)
# ===============================
events = {
    "2026-5-5": "어린이날",
    "2026-5-21": "중간고사",
    "2026-5-28": "체육대회",
}

st.title("📅 울산공업고등학교 일정 달력")

year = 2026
month = st.slider("월 선택", 1, 12, 5)

weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
cal = calendar.monthcalendar(year, month)

fig, ax = plt.subplots(figsize=(14, 6))
ax.set_xlim(0, 7)
ax.set_ylim(0, len(cal) + 1)
ax.axis("off")

# 요일
for i, day in enumerate(weekdays):
    ax.text(i + 0.5, len(cal) + 0.5, day, ha="center", va="center", fontsize=13, fontproperties=font_prop)

# 날짜
for row, week in enumerate(cal):
    y = len(cal) - row - 1
    for col, d in enumerate(week):
        if d == 0:
            ax.add_patch(plt.Rectangle((col, y), 1, 1, fill=False))
            continue

        key = f"{year}-{month}-{d}"
        color = "#FFF3B0" if key in events else "white"

        ax.add_patch(plt.Rectangle((col, y), 1, 1, facecolor=color, edgecolor="black"))
        ax.text(col + 0.05, y + 0.75, str(d), fontsize=12)

        if key in events:
            ax.text(
                col + 0.05,
                y + 0.4,
                events[key],
                fontsize=10,
                fontproperties=font_prop,
            )

st.pyplot(fig)
