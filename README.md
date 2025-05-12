echo "# CRM Tool Project" > README.md
echo "A terminal-based CRM tool using PostgreSQL." >> README.md
echo " " >> README.md
echo "## How to Run"  >> README.md
echo "1.  Install PostgreSQL and create a database named 'crm_tool'."  >> README.md
echo "2.  Run the SQL script (crm_tool.sql) to create the tables." >> README.md
echo "3.  Install psycopg2 (if using the Python script): `pip install psycopg2-binary`"  >> README.md
echo "4.  Run the Python script: `python crm_tool.py`"  >> README.md
git add README.md
git commit -m "Add README"
