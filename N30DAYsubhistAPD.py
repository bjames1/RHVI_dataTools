from basicInfo import *

# gsheetVars

substanceInfo = pd.read_pickle("./substanceInfo.pkl");

dataDict_N30DAYsubhistAPD = {};


for ithSubstance in range(nSubstances):

    fieldNames=[];
    SUBSTANCE = substance_list[ithSubstance];
    itemPREFIX = N30DAYsubhistAPD_DICT['survey_item_prefix'][0];
    ITEM = {SUBSTANCE: {'survey_item_prefix':itemPREFIX}}
    dataDict_N30DAYsubhistAPD.update(ITEM)

    for prefix in N30DAYsubhistYN_DICT['field_name_prefixes']:
        fieldPREFIX = N30DAYsubhistYN_DICT['field_name_prefixes'][prefix];
        FIELD_NAME = itemPREFIX + fieldPREFIX + SUBSTANCE;
        fieldNames.append(FIELD_NAME)
    dataDict_N30DAYsubhistAPD.update({SUBSTANCE: {'field_names':fieldNames}})

    for fieldName in dataDict_N30DAYsubhistAPD[SUBSTANCE]['field_names']:
        index = fieldNames.index(fieldName);

        OBJECT_CONTENTS = N30DAYsubhistAPD_DICT['object_contents'][index];
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('TITLE', substance_index(ithSubstance, 't'));
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('LOWER', substance_index(ithSubstance, 'l'));
        dataDict_N30DAYsubhistAPD[SUBSTANCE][fieldName] = OBJECT_CONTENTS;

    for exampleType in exampleTypes:
        substanceInfo[SUBSTANCE][exampleType];
        exampleList=substanceInfo[SUBSTANCE][exampleType];
        examplePREFIX = itemPREFIX + '_' + exampleType + '_' + SUBSTANCE;
        del dataDict_N30DAYsubhistAPD[SUBSTANCE][examplePREFIX]
        dataDict_N30DAYsubhistAPD[SUBSTANCE][examplePREFIX]=exampleList;


dataDict_N30DAYsubhistAPD = pd.DataFrame.from_dict(dataDict_N30DAYsubhistAPD);
dataDict_N30DAYsubhistAPD.to_pickle("./dataDict_N30DAYsubhistAPD.pkl")
# dataDict_N30DAYsubhistAPD = pd.read_pickle("./dataDict_N30DAYsubhistAPD.pkl");
# dataDict_N30DAYsubhistAPD.to_excel("RVHIdatabase_N30DAYsubhistYN_dataDictionary.xlsx");
