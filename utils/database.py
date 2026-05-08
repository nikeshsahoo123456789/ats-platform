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
    # DELETED CANDIDATES TABLE
    # =================================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS deleted_candidates (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        original_id INTEGER,

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
# FETCH DELETED CANDIDATES
# =====================================================

def fetch_deleted_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT
        original_id,
        Name,
        Email,
        Role,
        Experience,
        Skills,
        CurrentSalary,
        ExpectedSalary,
        ReferredBy,
        EmployeeID,
        Qualification,
        Location,
        Status,
        Resume

    FROM deleted_candidates

    ORDER BY id DESC

    """)

    data = cursor.fetchall()

    conn.close()

    return data

# =====================================================
# REMOVE CANDIDATE
# =====================================================

def remove_candidate(candidate_id):

    conn = get_connection()

    cursor = conn.cursor()

    # =============================================
    # FETCH CANDIDATE
    # =============================================

    cursor.execute("""

    SELECT * FROM candidates
    WHERE id = ?

    """,

    (candidate_id,))

    candidate = cursor.fetchone()

    if candidate:

        # =========================================
        # MOVE TO DELETED TABLE
        # =========================================

        cursor.execute("""

        INSERT INTO deleted_candidates (

            original_id,
            Name,
            Email,
            Role,
            Experience,
            Skills,
            CurrentSalary,
            ExpectedSalary,
            ReferredBy,
            EmployeeID,
            Qualification,
            Location,
            Status,
            Resume

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        (

            candidate[0],
            candidate[1],
            candidate[2],
            candidate[3],
            candidate[4],
            candidate[5],
            candidate[6],
            candidate[7],
            candidate[8],
            candidate[9],
            candidate[10],
            candidate[11],
            candidate[12],
            candidate[13]

        ))

        # =========================================
        # DELETE FROM MAIN TABLE
        # =========================================

        cursor.execute("""

        DELETE FROM candidates
        WHERE id = ?

        """,

        (candidate_id,))

    conn.commit()

    conn.close()

# =====================================================
# RESTORE CANDIDATE
# =====================================================

def restore_candidate(candidate_id):

    conn = get_connection()

    cursor = conn.cursor()

    # =============================================
    # FETCH DELETED CANDIDATE
    # =============================================

    cursor.execute("""

    SELECT
        original_id,
        Name,
        Email,
        Role,
        Experience,
        Skills,
        CurrentSalary,
        ExpectedSalary,
        ReferredBy,
        EmployeeID,
        Qualification,
        Location,
        Status,
        Resume

    FROM deleted_candidates

    WHERE original_id = ?

    """,

    (candidate_id,))

    candidate = cursor.fetchone()

    if candidate:

        # =========================================
        # RESTORE TO MAIN TABLE
        # =========================================

        cursor.execute("""

        INSERT INTO candidates (

            id,
            Name,
            Email,
            Role,
            Experience,
            Skills,
            CurrentSalary,
            ExpectedSalary,
            ReferredBy,
            EmployeeID,
            Qualification,
            Location,
            Status,
            Resume

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        """,

        candidate)

        # =========================================
        # REMOVE FROM DELETED TABLE
        # =========================================

        cursor.execute("""

        DELETE FROM deleted_candidates
        WHERE original_id = ?

        """,

        (candidate_id,))

    conn.commit()

    conn.close()

# =====================================================
# DELETE CANDIDATE PERMANENTLY
# =====================================================

def permanently_delete_candidate(candidate_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    DELETE FROM deleted_candidates
    WHERE original_id = ?

    """,

    (candidate_id,))

    conn.commit()

    conn.close()

# =====================================================
# INITIALIZE DATABASE
# =====================================================

create_tables()