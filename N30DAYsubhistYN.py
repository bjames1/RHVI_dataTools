from basicInfo import *

# gsheetVars

substanceInfo = pd.read_pickle("./substanceInfo.pkl");

dataDict = {};

for ithSubstance in range(nSubstances):

    fieldNames=[];
    SUBSTANCE = substance_list[ithSubstance];
    itemPREFIX = N30DAYsubhistYN_DICT['survey_item_prefix'][0];
    ITEM = {SUBSTANCE: {'survey_item_prefix':itemPREFIX}}
    dataDict.update(ITEM)

    for prefix in N30DAYsubhistYN_DICT['field_name_prefixes']:
        fieldPREFIX = N30DAYsubhistYN_DICT['field_name_prefixes'][prefix];
        FIELD_NAME = itemPREFIX + fieldPREFIX + SUBSTANCE;
        fieldNames.append(FIELD_NAME)
    dataDict.update({SUBSTANCE: {'field_names':fieldNames}})

    for fieldName in dataDict[SUBSTANCE]['field_names']:
        index = fieldNames.index(fieldName);
        OBJECT_CONTENTS = N30DAYsubhistYN_DICT['object_contents'][index];
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('TITLE', substance_index(ithSubstance, 't'));
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('LOWER', substance_index(ithSubstance, 'l'));
        dataDict[SUBSTANCE][fieldName] = OBJECT_CONTENTS;

    for exampleType in exampleTypes:
        substanceInfo[SUBSTANCE][exampleType];
        exampleList=substanceInfo[SUBSTANCE][exampleType];
        examplePREFIX = itemPREFIX + '_' + exampleType + '_' + SUBSTANCE;
        del dataDict[SUBSTANCE][examplePREFIX]
        dataDict[SUBSTANCE][examplePREFIX]=exampleList;


# dataDict = pd.DataFrame.from_dict(dataDict);
# dataDict.to_pickle("./dataDict.pkl")
# dataDict = pd.read_pickle("./dataDict.pkl");
# dataDict.to_excel("RVHIdatabase_N30DAYsubhistYN_dataDictionary.xlsx");
