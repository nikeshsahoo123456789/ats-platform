import sqlite3

DB_NAME = "candidates.db"

# =====================================================
# DATABASE CONNECTION
# =====================================================

def get_connection():

    return sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )

# =====================================================
# CREATE TABLES
# =====================================================

def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    # =================================================
    # CANDIDATES TABLE
    # =================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS candidates (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        Name TEXT,
        Email TEXT,
        Role TEXT,
        Experience TEXT,
        Skills TEXT,
        CurrentSalary TEXT,
        ExpectedSalary TEXT,
        ReferredBy TEXT,
        EmployeeID TEXT,
        Qualification TEXT,
        Location TEXT,
        Status TEXT,
        Resume TEXT

    )

    """)

    # =================================================
    # MRF TABLE
    # =================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS mrf (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        Position TEXT,
        Department TEXT,
        Branch TEXT,
        CandidateType TEXT,
        Vacancies TEXT,
        Reason TEXT,
        Experience TEXT,
        WorkMode TEXT,
        JobDescription TEXT,
        Status TEXT,
        CreatedDate TEXT

    )

    """)

    conn.commit()

    conn.close()

# =====================================================
# FETCH ALL CANDIDATES
# =====================================================

def fetch_all():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM candidates
    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data

# =====================================================
# FETCH ALL MRFS
# =====================================================

def fetch_all_mrf():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT * FROM mrf
    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data

# =====================================================
# INITIALIZE DATABASE
# =====================================================

create_tables()