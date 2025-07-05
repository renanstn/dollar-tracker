#!/bin/bash

# Mostra valores salvos no DB.

DB_PATH="dollar.db"
QUERY="SELECT id, datehour, value FROM dollar ORDER BY datehour DESC;"
sqlite3 -header -column "$DB_PATH" "$QUERY"

# -header: Show header on view
# -column: separate results by better columns
