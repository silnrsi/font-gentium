# Copyright (c) 2007-2025 SIL Global  (https://www.sil.org)
# Released under the MIT License (https://opensource.org/licenses/MIT)

import sys, csv, re

if sys.argv[1].lower() != "andika":
    andika_f = 0
else:
    andika_f = 1

if sys.argv[1].lower() != "gentium":
    gentium_f = 0
else:
    gentium_f = 1

glyph_data_csv_fn = "glyph_data.csv"

# andika_f = 0
if not andika_f:
    gsi_fn = "gsi_glyph_data_cdg.xml"
else:
    gsi_fn = "gsi_glyph_data_a.xml"

csv_cols = ["glyph_name", "ps_name", "sort_final_cdg", "sort_final_a", "assoc_feat_cdg", "assoc_feat_a", "assoc_feat_val", "assoc_uids_cdg", "assoc_uids_a"]

gsi_xml_start = '''\
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE font SYSTEM "gsi.dtd">
<font>'''

gsi_xml_end = '''
</font>
'''

gsi_xml_tmplt_start = '''
	<glyph active="1" contour="T1" sort="{sort}" name="{name}">
		<ps_name value="{ps_name}"/>'''

gsi_xml_tmplt_var_uid = '''
		<var_uid>{var_uid}</var_uid>'''

gsi_xml_tmplt_lig_uid = '''
		<lig_uid>{lig_uid}</lig_uid>'''

gsi_xml_tmplt_feat_cat = '''
		<feature category="{category}"/>'''

gsi_xml_tmplt_feat_cat_val = '''
		<feature category="{category}" value="{value}"/>'''

gsi_xml_tmplt_end = '''
	</glyph>'''

gsi_xml_tmplt_1 = '''
	<glyph active="1" contour="T1" sort="{sort}" name="{name}">
		<ps_name value="{ps_name}"/>
		<var_uid>{var_uid}</var_uid>
		<feature category="{category}"/>
	</glyph>
'''

gsi_xml_tmplt_2 = '''
	<glyph active="1" contour="T1" sort="{sort}" name="{name}">
		<ps_name value="{ps_name}"/>
		<var_uid>{var_uid}</var_uid>
		<feature category="{category}" value="{value}"/>
	</glyph>
'''

gsi_xml = open(gsi_fn, "w")
glyph_data_csv = open(glyph_data_csv_fn, newline='')

glyph_name = "glyph_name"
ps_name = "ps_name"
assoc_feat_val = "assoc_feat_val"
sort_final = "sort_final_cdg" if not andika_f else "sort_final_a"
assoc_uids = "assoc_uids_cdg" if not andika_f else "assoc_uids_a"
assoc_feat = "assoc_feat_cdg" if not andika_f else "assoc_feat_a"

glyph_data_reader = csv.reader(glyph_data_csv)
row = next(glyph_data_reader)
if (row != csv_cols):
    print(row)
    sys.exit()

gsi_xml.write(gsi_xml_start)

ct = 0
for row_file in glyph_data_reader:
    # smcp is the only feature that spans families and that affects different USVs in those families
    # if non-Gentium font, filter out smcp glyphs associated with Greek USVs
    #   except for Greek Symbols (eg GrThetaSym.sc) that are in non-Gentium fonts
    #   Greek USVs: 0370-03FF, 1F00-1FFF (includes some coptic, which are not currently in CDGA fonts)
    if not gentium_f:
        if row_file[csv_cols.index(assoc_feat)] == 'smcp':
            assoc_uid_str = row_file[csv_cols.index(assoc_uids)]
            if assoc_uid_str and not " " in assoc_uid_str:
                uid = int(assoc_uid_str, 16)
                if (uid >= 0x0370 and uid <= 0x03FF) or (uid >= 0x1F00 and uid <= 0x1FFF):
                    if not re.search(r"Gr.*Sym", row_file[csv_cols.index(glyph_name)]):
                        continue

    ct += 1
    rows_temp = [list(row_file)]
    if row_file[csv_cols.index(assoc_feat)] == "ss01":
        glyph_nm = row_file[csv_cols.index(glyph_name)]
        if not andika_f:
            if re.search(r"\.SngStory", glyph_nm):
                row_file[csv_cols.index(assoc_feat)] = "ss11"
            elif re.search(r"\.SngBowl", glyph_nm):
                row_file[csv_cols.index(assoc_feat)] = "ss12"
        else:
            if re.search("SmA|FemOrd", glyph_nm):
                row_file[csv_cols.index(assoc_feat)] = "ss13"
            elif re.search("SmG", glyph_nm):
                row_file[csv_cols.index(assoc_feat)] = "ss14"
        rows_temp.append(row_file)
    for row in rows_temp:
        glyph_data_dict = {"sort" : row[csv_cols.index(sort_final)], 
                           "name" : row[csv_cols.index(glyph_name)], 
                           "ps_name" : row[csv_cols.index(ps_name)], 
                          }
        gsi_xml.write(gsi_xml_tmplt_start.format(**glyph_data_dict))
    
        if row[csv_cols.index(assoc_uids)]:
            var_uid_str = row[csv_cols.index(assoc_uids)] # can be space delimited list
            var_uid = "U+" + " U+".join(var_uid_str.strip().split())
            if not " " in var_uid_str:
                glyph_data_dict["var_uid"] = var_uid
                gsi_xml.write(gsi_xml_tmplt_var_uid.format(**glyph_data_dict))
            else:
                glyph_data_dict["lig_uid"] = var_uid        
                gsi_xml.write(gsi_xml_tmplt_lig_uid.format(**glyph_data_dict))
                
        if row[csv_cols.index(assoc_feat)]:
            glyph_data_dict["category"] = row[csv_cols.index(assoc_feat)]
    
        if row[csv_cols.index(assoc_feat_val)]:
            glyph_data_dict["value"] = row[csv_cols.index(assoc_feat_val)]
            assert("category" in glyph_data_dict)
            gsi_xml.write(gsi_xml_tmplt_feat_cat_val.format(**glyph_data_dict))
        elif "category" in glyph_data_dict:
            gsi_xml.write(gsi_xml_tmplt_feat_cat.format(**glyph_data_dict))
        else:
            pass

        gsi_xml.write(gsi_xml_tmplt_end)
print("gsi records generated: {}\n".format(ct))

gsi_xml.write(gsi_xml_end)

glyph_data_csv.close()
gsi_xml.close()