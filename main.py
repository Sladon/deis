from web.data_handler import WebData
from web.web_file import WebFile

DATA_URL = 'https://deis.minsal.cl/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=2889&target_action=get-all-data'

web_data = WebData(DATA_URL)

options = web_data.get_options()
for i in range(len(options)):
    print(i, options[i]['name'])

DEF_1990_2020 = web_data.get_option_information(22, options)
DEF_2021_2023 = web_data.get_option_information(23, options)

def_1990_2020 = WebFile(DEF_1990_2020[0], DEF_1990_2020[1], DEF_1990_2020[2])
def_2021_2023 = WebFile(DEF_2021_2023[0], DEF_2021_2023[1], DEF_2021_2023[2])

def_1990_2020.extract()
def_2021_2023.extract()