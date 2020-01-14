import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [ \

        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"

        ];

creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds);

sheet = client.open("RVHIdatabase_variableListing")


# worksheets[0]
# worksheets[1]
# worksheets[2]
# worksheets[3]
# worksheets[4]
# worksheets[5]
# worksheets[6]

DemographicInfo_WS = sheet.get_worksheet(0);
SubstancesList_WS = sheet.get_worksheet(2);
N30DAYsubhistYN_WS = sheet.get_worksheet(1);
N30DAYsubhistAPD_WS = sheet.get_worksheet(3);
N30DAYsubhistTPD_WS = sheet.get_worksheet(4);
N30DAYsubhistDPM_WS = sheet.get_worksheet(5);
N30DAYsubhistUM_WS = sheet.get_worksheet(6);

DemographicInfo_TABLE = DemographicInfo_WS.get_all_values();
SubstancesList_TABLE = SubstancesList_WS.get_all_values();
N30DAYsubhistYN_TABLE = N30DAYsubhistYN_WS.get_all_values();
N30DAYsubhistAPD_TABLE = N30DAYsubhistAPD_WS.get_all_values();
N30DAYsubhistTPD_TABLE = N30DAYsubhistTPD_WS.get_all_values();
N30DAYsubhistDPM_TABLE = N30DAYsubhistDPM_WS.get_all_values();
N30DAYsubhistUM_TABLE = N30DAYsubhistUM_WS.get_all_values();


##Convert table data into a dataframe
DemographicInfo = pd.DataFrame(DemographicInfo_TABLE[1:], columns=DemographicInfo_TABLE[0]);
SubstancesList = pd.DataFrame(SubstancesList_TABLE[1:], columns=SubstancesList_TABLE[0]);
N30DAYsubhistYN = pd.DataFrame(N30DAYsubhistYN_TABLE[1:], columns=N30DAYsubhistYN_TABLE[0]);
N30DAYsubhistAPD = pd.DataFrame(N30DAYsubhistAPD_TABLE[1:], columns=N30DAYsubhistAPD_TABLE[0]);
N30DAYsubhistTPD = pd.DataFrame(N30DAYsubhistTPD_TABLE[1:], columns=N30DAYsubhistTPD_TABLE[0]);
N30DAYsubhistDPM = pd.DataFrame(N30DAYsubhistDPM_TABLE[1:], columns=N30DAYsubhistDPM_TABLE[0]);
N30DAYsubhistUM = pd.DataFrame(N30DAYsubhistUM_TABLE[1:], columns=N30DAYsubhistUM_TABLE[0]);


# DemographicInfo
#
# SubstancesList
#
# N30DAYsubhistYN
#
# N30DAYsubhistAPD
#
# N30DAYsubhistTPD
#
# N30DAYsubhistDPM
#
# N30DAYsubhistUM
