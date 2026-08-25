import sqlite3
import re
import pytest

def get_db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    with open('schema.sql', 'r') as f:
        sql_script = f.read()
    
    # Strip single-line SQL comments
    clean_script = re.sub(r'--.*', '', sql_script)
    
    # Split queries by semicolon
    statements = [stmt.strip() for stmt in clean_script.split(';') if stmt.strip()]
    
    # Extract SELECT statements
    select_statements = [stmt for stmt in statements if stmt.upper().startswith("SELECT")]
    
    # Run setup tables and inserts
    setup_statements = [stmt for stmt in statements if not stmt.upper().startswith("SELECT")]
    for stmt in setup_statements:
        cursor.execute(stmt)
        
    return conn, cursor, select_statements

def test_left_join():
    conn, cursor, select_statements = get_db_connection()
    if len(select_statements) < 1:
        pytest.fail("Missing Query: Please write the LEFT JOIN query in schema.sql")
    
    cursor.execute(select_statements[0])
    results = cursor.fetchall()
    assert len(results) == 4, f"Expected 4 rows, got {len(results)}"

def test_right_join():
    conn, cursor, select_statements = get_db_connection()
    if len(select_statements) < 2:
        pytest.fail("Missing Query: Please write the RIGHT JOIN query in schema.sql")
    
    cursor.execute(select_statements[1])
    results = cursor.fetchall()
    assert len(results) == 4, f"Expected 4 rows, got {len(results)}"
