import streamlit as st
import calendar
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl

# ---------------------------
# 한글 폰트 설정 (Streamlit Cloud 대응)
# ---------------------------
font_path = fm.findfont(fm.FontProperties(family='DejaVu Sans'))
mpl.rcParams["font.family"] = font_path
mpl.rcParams["axes.unicode_minus"] = False

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(layout="wide")
calendar.setfirstweekday(calendar.MONDAY)

# ---------------------------
# 울산공업고등학교 일정
# ---------------------------
EVENTS = {
    "2026-5-5": "어린이날",
    "2026-5-15": "학교 축제",
    "2026-6-20": "기말고사",
}

# ---------------------------
# 제목
# ---------------------------
st.title("📅 울산공업고등학교 일정 달력")

year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 5)

cal = calendar.monthcalendar(year, month)

# ✅ 달력 크기 줄임
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 7)
ax.set_ylim(0, len(cal) + 1)
ax.axis("off")

# ---------------------------
# 요일 표시 (월~일)
# ---------------------------
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
for i, day in enumerate(weekdays):
    ax.text(
        i + 0.5,
        len(cal) + 0.4,
        day,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold"
    )

# ---------------------------
# 날짜 & 일정
# ---------------------------
for w, week in enumerate(cal):
    for d, day in enumerate(week):
        if day == 0:
            continue

        y = len(cal) - w - 0.5
        x = d

        key = f"{year}-{month}-{day}"
        event = EVENTS.get(key)

        # 일정 있는 날 → 노란색
        if event:
            ax.add_patch(
                plt.Rectangle((x, y - 0.5), 1, 1, color="#FFE699")
            )

        # 날짜 숫자
        ax.text(
            x + 0.05,
            y + 0.25,
            str(day),
            fontsize=14,
            fontweight="bold",
            va="top"
        )

        # ✅ 일정 이름 칸 안에 표시
        if event:
            ax.text(
                x + 0.05,
                y - 0.05,
                event,
                fontsize=10,
                va="top",
                wrap=True
            )

st.pyplot(fig)
