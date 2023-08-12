from pathlib import Path
import subprocess

DOCUMENTS_DIR = Path(subprocess.run(['xdg-user-dir', 'DOCUMENTS'], capture_output=True, text=True).stdout.strip())
PROJECT_DIR = DOCUMENTS_DIR.joinpath(r'DEIS 2023')
DATA_DIR = PROJECT_DIR.joinpath(r'data')
RESULTS_DIR = DATA_DIR.joinpath(r'results')
DICTIONARIES_DIR = RESULTS_DIR.joinpath(r'dictionaries')
CSV_DIR = DATA_DIR.joinpath(r'CSVs')


# User paths where the files will be saved
PATHS = {
    'results': RESULTS_DIR,
    'dictionaries': DICTIONARIES_DIR,
    'csvs': CSV_DIR
}
