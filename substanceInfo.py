from basicInfo import *

# gsheetVars

# creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# client = gspread.authorize(creds);

SubstanceInfo_WS = client.open("substanceInfo");
sheet_count = len(SubstanceInfo_WS.worksheets());

dataDict_substanceInfo = {};

for sheet in range(sheet_count):
    SUBSTANCE = substance_index(sheet, 'u');

    ws = SubstanceInfo_WS.get_worksheet(sheet);
    table = ws.get_all_values();
    df = pd.DataFrame(table[1:], columns=table[0]);

    genericNames = df['genericNames'].values.tolist()
    genericNames = ' '.join(genericNames).split()

    brandNames = df['brandNames'].values.tolist()
    brandNames = ' '.join(brandNames).split()

    aliasNames = df['aliasNames'].values.tolist()
    aliasNames = ' '.join(aliasNames).split()

    apdQContents = df['apdQContents'].values.tolist()
    apdQContents = list(filter(None, apdQContents))

    apdUnits = df['apdUnits'].values.tolist()
    apdUnits = list(filter(None, apdUnits))

    exampleInfo = {SUBSTANCE: {

                                'genericNames':genericNames,
                                'brandNames':brandNames,
                                'aliasNames':aliasNames,
                                'apdQContents':apdQContents,
                                'apdUnits':apdUnits,

                                }};

    dataDict_substanceInfo.update(exampleInfo);


# import pandas as pd
dataDict_substanceInfo = pd.DataFrame.from_dict(dataDict_substanceInfo);
dataDict_substanceInfo.to_pickle("./dataDict_substanceInfo.pkl")
# dataDict_substanceInfo = pd.read_pickle("./dataDict_substanceInfo.pkl");
# dataDict_substanceInfo.to_excel("RVHIdatabase_dataDict_substanceInfo_dataDict_substanceInfo.xlsx");
