from web.data_handler import WebData
from web.file import File
from global_params.paths import PATHS
from os import listdir, path
from data.data_handler import HandleCSV

## STOPPED WORKING 23/11/2023, requires to download files manually
# DATA_URL = 'https://deis.minsal.cl/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=2889&target_action=get-all-data'

# web_data = WebData(DATA_URL)

# options = web_data.get_options()
# for i in range(len(options)):
#     print(i, options[i]['name'])

# DEF_1990_2020 = web_data.get_option_information(22, options)
# DEF_2021_2023 = web_data.get_option_information(23, options)

# def_1990_2020 = WebFile(DEF_1990_2020[0], DEF_1990_2020[1], DEF_1990_2020[2])
# def_2021_2023 = WebFile(DEF_2021_2023[0], DEF_2021_2023[1], DEF_2021_2023[2])

RAW_CSV_DIR = PATHS["raw"]
csvs = [f for f in listdir(RAW_CSV_DIR) if path.isfile(path.join(RAW_CSV_DIR, f)) and not f.startswith('.')]
csvs_handlers = [HandleCSV(RAW_CSV_DIR.joinpath(r"".join(csv))) for csv in csvs]


for csv_handler in csvs_handlers:
    csv_handler.save_dfs_by_year_to_dir()