# CHECKING AVAILABLE DRIVERS...

import pyodbc

msa_drivers = [x for x in pyodbc.drivers() if "ACCESS" in x.upper()]
print(f"MS-ACCESS drivers : {msa_drivers}")
