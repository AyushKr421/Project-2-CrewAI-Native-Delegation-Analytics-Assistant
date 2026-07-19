from function_tools.analyst_tools import validate_sql_safety

print(validate_sql_safety("SELECT * FROM sales"))
print(validate_sql_safety("DELETE FROM sales"))