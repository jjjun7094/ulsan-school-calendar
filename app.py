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
# 학사 일정 (한국어)
# ---------------------------
events = {
    "2026-03-02": "1학기 개학 / 입학식",
    "2026-04-10": "중간고사",
    "2026-05-05": "어린이날",
    "2026-05-21": "체육대회",
    "2026-06-10": "기말고사",
    "2026-06-23": "여름방학",
    "2026-09-01": "2학기 개학",
    "2026-10-20": "중간고사",
    "2026-12-08": "기말고사",
}

# ---------------------------
# 제목 / 선택
# ---------------------------
st.title("🏫 울산공업고등학교 일정 달력")

year = st.selectbox("연도 선택", [2026])
month = st.slider("월 선택", 1, 12, 5)

# ---------------------------
# 요일 (한국어)
# ---------------------------
cols = st.columns(7)
weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

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

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.axis("off")

    table_data = []

    for week in cal:
        row = []
        for day in week:
            if day == 0:
                row.append("")
            else:
                # ✅ 핵심 수정 부분 (일정 한국어 정상 출력)
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
    table.set_fontsize(11)
    table.scale(1.2, 2.0)

    # 주말 색
    for r in range(len(table_data)):
        table[r, 5].set_facecolor("#E8F1FF")  # 토요일
        table[r, 6].set_facecolor("#FFECEC")  # 일요일

    # 일정 있는 날 색
    for r, week in enumerate(cal):
        for c, day in enumerate(week):
            if day != 0:
                key = f"{year}-{month:02d}-{day:02d}"
                if key in events:
                    table[r, c].set_facecolor("#FFF3B0")

    ax.set_title(f"{year}년 {month}월", fontsize=16, pad=10)
    st.pyplot(fig)

draw_calendar(year, month)
