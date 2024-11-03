import streamlit as st
import subprocess
import time
import pandas as pd
from data import Database

# Initialize Streamlit session
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = time.time()
if 'game_running' not in st.session_state:
    st.session_state.game_running = False

def run_game():
    # Start the game and set the game_running state
    st.session_state.game_running = True
    process = subprocess.Popen(['python', 'main.py'])
    
    # Wait for the game to close
    process.wait()  # This will block until the game window is closed
    st.session_state.game_running = False

# Page config
st.set_page_config(
    page_title="Snake Game Dashboard",
    page_icon="🐍",
    layout="wide"
)

# Header
st.title("🐍 Classic Snake Game")
st.markdown("### 🎮 Game Statistics and Analytics")

# Play Button Styling
st.markdown(""" 
<style>
.stButton > button {
    height: 50px;
    width: 150px;
    background-color: #4CAF50;
    color: white;
    font-size: 20px;
    border: none;
    border-radius: 25px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.stButton > button:hover {
    background-color: #3c763d;
}
</style>
""", unsafe_allow_html=True)

# Play button
if st.button('🎮 Play Game', use_container_width=True) and not st.session_state.game_running:
    run_game()
    st.success("Game launched! The game window should open shortly...")

# message when the game is not running
if not st.session_state.game_running:
    st.success("Start a new game.")

# Ensure database is created
Database.create_db()

# Create columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader('🏆 Top 10 High Scores')
    scores = Database.get_scores()
    if scores:
        df = pd.DataFrame(scores, columns=['Score', 'Player', 'Date'])
        df = df.sort_values('Score', ascending=False)
        df.index = range(1, len(df) + 1)

        def highlight_top_three(row):
            color = '#FFD70022' if row.name <= 3 else ''
            return [f'background-color: {color}' for _ in row]

        styled_df = df.style.apply(highlight_top_three, axis=1)
        st.table(styled_df)
    else:
        st.info("No scores recorded yet! Be the first to play! 🎮")

with col2:
    st.subheader("📊 Today's Statistics")
    top_score_today = Database.get_todays_top_score()
    
    if top_score_today == 0:
        st.info("Nobody has played today. You can be the first! 🎯")
    else:
        col_metric1, col_metric2 = st.columns(2)
        with col_metric1:
            st.metric(
                label="Today's Best",
                value=f"{top_score_today}",
                delta="points"
            )
        with col_metric2:
            avg_score = sum(score[0] for score in scores) / len(scores) if scores else 0
            st.metric(
                label="Average Score",
                value=f"{avg_score:.1f}"
            )

# Time of Day stats
st.subheader("📈 Performance by Time of Day")
hourly_stats = Database.get_scores_by_time_of_day()
if hourly_stats:
    df = pd.DataFrame(hourly_stats)

    def style_dataframe(df):
        styles = pd.DataFrame('', index=df.index, columns=df.columns)
        styles['Top Score'] = 'background-color: #3c763d;'  # Dark green
        styles['Average Score'] = 'background-color: #31708f;'  # Dark blue
        styles['Lowest Score'] = 'background-color: #a94442;'  # Dark red
        return styles

    styled_df = df.style.apply(style_dataframe, axis=None)
    st.table(styled_df)
else:
    st.info("No hourly data available yet!")

# Weekly stats
st.subheader("📅 Performance by Day of Week")
daily_stats = Database.get_scores_by_day_of_week()
if daily_stats:
    df = pd.DataFrame(daily_stats)
    styled_df = df.style.apply(style_dataframe, axis=None)
    st.table(styled_df)
else:
    st.info("No weekly data available yet!")

# Additional Stats
if scores:
    st.subheader("📊 Overall Statistics")
    stats_col1, stats_col2, stats_col3 = st.columns(3)

    with stats_col1:
        st.metric(
            "Total Games",
            len(scores)
        )
    
    with stats_col2:
        st.metric(
            "Highest Score",
            max(score[0] for score in scores)
        )
        
    with stats_col3:
        st.metric(
            "Average Score",
            f"{sum(score[0] for score in scores) / len(scores):.1f}"
        )

# Auto-refresh logic
try:
    current_time = time.time()
    if current_time - st.session_state.last_refresh >= 5:
        st.session_state.last_refresh = current_time
        st.rerun()
except Exception as e:
    st.error(f"Error refreshing the page: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        Made with ❤️ by Cameron S.
    </div>
    """, 
    unsafe_allow_html=True
)
