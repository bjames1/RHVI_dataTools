from basicInfo import *

# gsheetVars

# creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
# client = gspread.authorize(creds);

SubstanceInfo_WS = client.open("substanceInfo");
sheet_count = len(SubstanceInfo_WS.worksheets());


substanceInfo = {};
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

    substanceInfo.update(exampleInfo);


# import pandas as pd
substanceInfo = pd.DataFrame.from_dict(substanceInfo);
substanceInfo.to_pickle("./substanceInfo.pkl")
# substanceInfo = pd.read_pickle("./substanceInfo.pkl");
# substanceInfo.to_excel("RVHIdatabase_substanceInfo_substanceInfo.xlsx");
