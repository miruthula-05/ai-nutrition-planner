from __future__ import annotations

import os
from typing import Any

import mysql.connector
from mysql.connector import Error


def get_db_config() -> dict[str, Any]:
    return {
        "host": os.getenv("MYSQL_HOST", "localhost"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", "ai_nutrition_planner"),
    }


def get_connection():
    config = get_db_config()
    return mysql.connector.connect(**config)


def init_database() -> None:
    config = get_db_config()
    database_name = config.pop("database")

    server_connection = mysql.connector.connect(**config)
    server_cursor = server_connection.cursor()
    server_cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`")
    server_cursor.close()
    server_connection.close()

    connection = mysql.connector.connect(database=database_name, **config)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone VARCHAR(50) NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


def create_user(name: str, email: str, phone: str, password_hash: str) -> tuple[bool, str]:
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            cursor.close()
            connection.close()
            return False, "An account with this email already exists."

        cursor.execute(
            """
            INSERT INTO users (name, email, phone, password_hash)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, phone, password_hash),
        )
        connection.commit()
        cursor.close()
        connection.close()
        return True, "Account created successfully."
    except Error as exc:
        return False, f"MySQL error: {exc}"


def get_user_by_email(email: str) -> dict[str, Any] | None:
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, name, email, phone, password_hash
            FROM users
            WHERE email = %s
            """,
            (email,),
        )
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user
    except Error:
        return None
