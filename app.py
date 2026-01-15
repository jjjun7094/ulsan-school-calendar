import streamlit as st
import calendar
import matplotlib.pyplot as plt
import matplotlib as mpl

# ---------------------------
# 기본 설정
# ---------------------------
st.set_page_config(page_title="울산공업고등학교 일정 달력", layout="wide")
calendar.setfirstweekday(calendar.MONDAY)
mpl.rcParams["axes.unicode_minus"] = False

# ---------------------------
# 2026년 학사 + 공휴일 일정
# ---------------------------
events = {
    # 1월
    "2026-01-01": "신정",
    "2026-01-09": "졸업식 / 종업식",
    "2026-01-10": "겨울방학",

    # 2월
    "2026-02-16": "설날연휴",
    "2026-02-17": "설날",
    "2026-02-18": "설날연휴",

    # 3월
    "2026-03-01": "삼일절",
    "2026-03-02": "1학기 개학 / 입학식",

    # 4월
    "2026-04-10": "중간고사",

    # 5월
    "2026-05-05": "어린이날",
    "2026-05-24": "부처님오신날",
    "2026-05-25": "대체공휴일",

    # 6월
    "2026-06-06": "현충일",
    "2026-06-10": "기말고사",
    "2026-06-23": "여름방학",

    # 8월
    "2026-08-15": "광복절",
    "2026-08-17": "대체공휴일",

    # 9월
    "2026-09-01": "2학기 개학",
    "2026-09-24": "추석연휴",
    "2026-09-25": "추석",
    "2026-09-26": "추석연휴",

    # 10월
    "2026-10-03": "개천절",
    "2026-10-05": "대체공휴일",
    "2026-10-09": "한글날",
    "2026-10-20": "중간고사",

    # 12월
    "2026-12-08": "기말고사",
    "2026-12-25": "성탄절",
}

# ---------------------------
# 제목
# ---------------------------
st.title("🏫 울산공업고등학교 2026 일정 달력")

year = 2026
month = st.slider("월 선택", 1, 12, 5)

# ---------------------------
# 요일 (한글)
# ---------------------------
cols = st.columns(7)
weekdays = ["월", "화", "수", "목", "금", "토", "일"]

for col, day in zip(cols, weekdays):
    col.markdown(
        f"<div style='text-align:center; font-weight:bold; font-size:18px;'>{day}</div>",
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------------------------
# 달력 그리기
# ---------------------------
def draw_calendar(year, month):
    cal = calendar.monthcalendar(year, month)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis("off")

    table_data = []
    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                key = f"{year}-{month:02d}-{day:02d}"
                if key in events:
                    row.append(f"{day}\n{events[key]}")
                else:
                    row.append(str(day))
        table_data.append(row)

    table = ax.table(
        cellText=table_data,
        cellLoc="left",
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.2)

    # 기본 색
    for r in range(len(table_data)):
        for c in range(7):
            table[r, c].set_facecolor("#111111")
            table[r, c].get_text().set_color("white")

    # 토요일 / 일요일
    for r in range(len(table_data)):
        table[r, 5].set_facecolor("#1f3a5f")  # 토
        table[r, 6].set_facecolor("#5f1f1f")  # 일

    # 일정 있는 날
    for r, week in enumerate(cal):
        for c, day in enumerate(week):
            if day != 0:
                key = f"{year}-{month:02d}-{day:02d}"
                if key in events:
                    table[r, c].set_facecolor("#fff3b0")
                    table[r, c].get_text().set_color("black")

    ax.set_title(f"{year}년 {month}월", fontsize=18, pad=15, color="white")
    fig.patch.set_facecolor("#0e1117")

    st.pyplot(fig)

draw_calendar(year, month)
