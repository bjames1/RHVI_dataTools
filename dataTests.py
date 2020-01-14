from gsheetData import *

# gsheetVars

dataDict = {};

for substance in range(nSubstances):

    fieldNames=[];
    SUBSTANCE = substance_list[substance];
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
        dataDict[SUBSTANCE][fieldName] = OBJECT_CONTENTS;

output = pd.DataFrame.from_dict(dataDict);
output.to_excel("RVHIdatabase_N30DAYsubhistYN_dataDictionary.xlsx");
