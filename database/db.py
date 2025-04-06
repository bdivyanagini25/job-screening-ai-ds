import sqlite3

def create_database():
    conn = sqlite3.connect('job_screening.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS candidates
                      (name TEXT, match_score REAL, job_description TEXT)''')
    conn.commit()
    conn.close()

def store_results(candidate_name, match_score, job_description):
    conn = sqlite3.connect('job_screening.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO candidates (name, match_score, job_description) VALUES (?, ?, ?)", 
                   (candidate_name, match_score, job_description))
    conn.commit()
    conn.close()
