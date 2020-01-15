from basicInfo import *

# gsheetVars

dataDict_substanceInfo = pd.read_pickle("./dataDict_substanceInfo.pkl");

dataDict_N30DAYsubhistUM = {};

for ithSubstance in range(nSubstances):

    fieldNames=[];
    SUBSTANCE = substance_list[ithSubstance];
    itemPREFIX = N30DAYsubhistUM_DICT['survey_item_prefix'][0];
    ITEM = {SUBSTANCE: {'survey_item_prefix':itemPREFIX}}
    dataDict_N30DAYsubhistUM.update(ITEM)

    for prefix in N30DAYsubhistUM_DICT['field_name_prefixes']:
        fieldPREFIX = N30DAYsubhistUM_DICT['field_name_prefixes'][prefix];
        FIELD_NAME = itemPREFIX + fieldPREFIX + SUBSTANCE;
        fieldNames.append(FIELD_NAME)
    dataDict_N30DAYsubhistUM.update({SUBSTANCE: {'field_names':fieldNames}})

    for fieldName in dataDict_N30DAYsubhistUM[SUBSTANCE]['field_names']:
        index = fieldNames.index(fieldName);

        OBJECT_CONTENTS = N30DAYsubhistUM_DICT['object_contents'][index];
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('TITLE', substance_index(ithSubstance, 't'));
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('LOWER', substance_index(ithSubstance, 'l'));
        OBJECT_CONTENTS = OBJECT_CONTENTS.replace('UPPER', substance_index(ithSubstance, 'u'));
        dataDict_N30DAYsubhistUM[SUBSTANCE][fieldName] = OBJECT_CONTENTS;


dataDict_N30DAYsubhistUM = pd.DataFrame.from_dict(dataDict_N30DAYsubhistUM);
dataDict_N30DAYsubhistUM.to_pickle("./dataDict_N30DAYsubhistUM.pkl")

# dataDict_N30DAYsubhistUM = pd.read_pickle("./dataDict_N30DAYsubhistUM.pkl");
# dataDict_N30DAYsubhistUM.to_excel("RVHIdatabase_N30DAYsubhistYN_dataDictionary.xlsx");
