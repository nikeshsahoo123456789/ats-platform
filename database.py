import sqlite3

DB_NAME = "candidates.db"

# =====================================================
# GET DATABASE CONNECTION
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

        name TEXT,

        email TEXT,

        role TEXT,

        experience INTEGER,

        skills TEXT,

        company TEXT,

        location TEXT,

        resume TEXT,

        status TEXT,

        created TEXT
    )
    """)

    # =================================================
    # MRF TABLE
    # =================================================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mrf (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        position TEXT,

        department TEXT,

        branch TEXT,

        type TEXT,

        vacancies TEXT,

        reason TEXT,

        status TEXT,

        applications INTEGER
    )
    """)

    conn.commit()

    conn.close()


# =====================================================
# INSERT CANDIDATE
# =====================================================

def insert_candidate(data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO candidates (

        name,
        email,
        role,
        experience,
        skills,
        company,
        location,
        resume,
        status,
        created

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

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
# UPDATE CANDIDATE STATUS
# =====================================================

def update_status(candidate_id, new_status):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE candidates
        SET status = ?
        WHERE id = ?
        """,
        (new_status, candidate_id)
    )

    conn.commit()

    conn.close()


# =====================================================
# DELETE CANDIDATE
# =====================================================

def delete_candidate(candidate_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM candidates
        WHERE id = ?
        """,
        (candidate_id,)
    )

    conn.commit()

    conn.close()


# =====================================================
# INSERT MRF
# =====================================================

def insert_mrf(data):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO mrf (

        position,
        department,
        branch,
        type,
        vacancies,
        reason,
        status,
        applications

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()

    conn.close()


# =====================================================
# FETCH ALL MRFS
# =====================================================

def get_all_mrfs():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT

        position,
        department,
        branch,
        type,
        vacancies,
        reason,
        status,
        applications

    FROM mrf

    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows