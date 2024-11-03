import sqlite3
import datetime

class Database():
    
    @staticmethod
    def create_db() -> None:
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores
        (id INTEGER PRIMARY KEY,
        score INTEGER,
        name TEXT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)                   
                    ''')
        
        conn.commit()
        conn.close()        
        
    @staticmethod
    def is_top_ten(score) -> bool:
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT score FROM scores
        ORDER BY score DESC
        LIMIT 10
                        ''')
        top_ten = cursor.fetchall()
        conn.close()
        
        if len(top_ten) < 10:
            return True
        
        lowest_top_ten = top_ten[-1][0]
        return score > lowest_top_ten
        
    @staticmethod
    def insert_score(score, name=None) -> None:
        conn = sqlite3.connect('snake_scores.db')
        if Database.is_top_ten(score):
            if name is None:
                name = "Anonymous"  # Set default name
            
                # You can collect the name using Streamlit if needed
                # Uncomment the following line if you want to get input directly
                # name = st.text_input("Enter your name:", value="Anonymous")

        else:
            name = "Anonymous"
            
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO scores (score, date, name) 
        VALUES (?, ?, ?)''',
        (score, current_date, name)
                    )

        conn.commit()
        conn.close()
        
    @staticmethod
    def get_scores() -> tuple:
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT
            score,
            name,
            strftime('%Y-%m-%d', date, 'localtime')
        FROM scores
        ORDER BY score DESC
        LIMIT 10
                    ''')
        
        scores = cursor.fetchall()
        conn.close()
        return scores
    
    @staticmethod
    def get_todays_top_score() -> int:
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
        cursor.execute('''
            SELECT MAX(score) 
            FROM scores 
            WHERE DATE(date) = DATE(?)
        ''', (current_date,))
        
        top_score = cursor.fetchone()[0]
        
        conn.close()
        return top_score or 0
    
    @staticmethod
    def get_scores_by_time_of_day():
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                strftime('%H', date) AS hour,
                GROUP_CONCAT(score) AS scores
            FROM scores
            GROUP BY hour
            ORDER BY hour
        ''')
        scores_by_hour = []
        for hour, score_string in cursor.fetchall():
            scores = [int(s) for s in score_string.split(',')]
            hour_int = int(hour)
            period = 'AM' if hour_int < 12 else 'PM'
            hour_12 = f"{hour_int % 12 or 12}:00 {period}"

            scores_by_hour.append({
                'Hour': hour_12,
                'Top Score': max(scores),
                'Average Score': round(sum(scores) / len(scores), 1),
                'Lowest Score': min(scores)
            })
        conn.close()
        return scores_by_hour

    @staticmethod
    def get_scores_by_day_of_week():
        conn = sqlite3.connect('snake_scores.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                strftime('%w', date) AS weekday,
                GROUP_CONCAT(score) AS scores
            FROM scores
            GROUP BY weekday
            ORDER BY weekday
        ''')
        days_labels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        scores_by_weekday = []
        for weekday, score_string in cursor.fetchall():
            scores = [int(s) for s in score_string.split(',')]
            scores_by_weekday.append({
                'Day': days_labels[int(weekday)],
                'Top Score': max(scores),
                'Average Score': round(sum(scores) / len(scores), 1),
                'Lowest Score': min(scores)
            })
        conn.close()
        return scores_by_weekday
