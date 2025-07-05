#!/bin/sh

psql "$DATABASE_URL" -c "SELECT * FROM dollar;"
