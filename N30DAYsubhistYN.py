from basicInfo import *

# gsheetVars

dataDict_substanceInfo = pd.read_pickle("./dataDict_substanceInfo.pkl");

dataDict_N30DAYsubhistYN = {};

for ithSubstance in range(nSubstances):

    fieldNames=[];
    SUBSTANCE = substance_list[ithSubstance];
    itemPREFIX = N30DAYsubhistYN_DICT['survey_item_prefix'][0];
    ITEM = {SUBSTANCE: {'survey_item_prefix':itemPREFIX}}
    dataDict_N30DAYsubhistYN.update(ITEM)

    for prefix in N30DAYsubhistYN_DICT['field_name_prefixes']:
        fieldPREFIX = N30DAYsubhistYN_DICT['field_name_prefixes'][prefix];
        FIELD_NAME = itemPREFIX + fieldPREFIX + SUBSTANCE;
        fieldNames.append(FIELD_NAME)
    dataDict_N30DAYsubhistYN.update({SUBSTANCE: {'field_names':fieldNames}})

    for fieldName in dataDict_N30DAYsubhistYN[SUBSTANCE]['field_names']:
        index = fieldNames.index(fieldName);
        OBJECT_CONTENTS = N30DAYsubhistYN_DICT['object_contents'][index];
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('TITLE', substance_index(ithSubstance, 't'));
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('LOWER', substance_index(ithSubstance, 'l'));
        # OBJECT_CONTENTS = OBJECT_CONTENTS.replace('UPPER', substance_index(ithSubstance, 'u'));
        dataDict_N30DAYsubhistYN[SUBSTANCE][fieldName] = OBJECT_CONTENTS;


    for exampleType in exampleTypes:
        dataDict_substanceInfo[SUBSTANCE][exampleType];
        exampleList=dataDict_substanceInfo[SUBSTANCE][exampleType];
        examplePREFIX = itemPREFIX + '_' + exampleType + '_' + SUBSTANCE;
        del dataDict_N30DAYsubhistYN[SUBSTANCE][examplePREFIX]
        dataDict_N30DAYsubhistYN[SUBSTANCE][examplePREFIX]=exampleList;


dataDict_N30DAYsubhistYN = pd.DataFrame.from_dict(dataDict_N30DAYsubhistYN);
dataDict_N30DAYsubhistYN.to_pickle("./dataDict_N30DAYsubhistYN.pkl")

# dataDict_N30DAYsubhistYN = pd.read_pickle("./dataDict_N30DAYsubhistYN.pkl");
# dataDict_N30DAYsubhistYN.to_excel("RVHIdatabase_N30DAYsubhistYN_dataDict_N30DAYsubhistYNionary.xlsx");
