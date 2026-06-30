import pandas as pd
from pathlib import Path

# Project root folder
base_dir = Path(__file__).resolve().parent

# Data folder path
data_dir = base_dir / "data"

# Load datasets
projects = pd.read_csv(data_dir / "projects.csv")
employees = pd.read_csv(data_dir / "employees.csv")
tasks = pd.read_csv(data_dir / "tasks.csv")
incidents = pd.read_csv(data_dir / "incidents.csv")
timesheets = pd.read_csv(data_dir / "timesheets.csv")