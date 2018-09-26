# languages
lang1 = 'de'  # translate from...
lang2 = 'en'  # to ...

# a list of keywords, to intersect with the second column of the translation list (the one that is the target language)
list_intersect = ['machine learning', 'artificial intelligence', 'neural network', 'data science']

# wWhen intersecting: exact matches only?
# Ff true, only exact matches in the intersection of df_langlinks and intersect are considered.
# If false, all entries that contain the specified keyword are considered (e.g. for keyword "neural network" also "artificial neural network" is included.)
intersect_exact = False

# directories
dir_original = "data/downloads/"   # downloaded sql files
dir_titles = "data/lists/"    # csv file of titles list
dir_langlinks = "data/lists/"    # csv file of language links
dir_final = "data/"        # csv file of final translation list

# this list can be created using modules.utils.create_lang_list
langs = ['aa', 'ab', 'ace', 'ady', 'af', 'ak', 'als', 'am', 'an', 'ang', 'ar', 'arc', 'arz', 'as', 'ast', 'atj', 'av', 'ay', 'az', 'azb', 'ba', 'bar', 'bcl', 'be', 'bg', 'bh', 'bi', 'bjn', 'bm', 'bn', 'bo', 'bpy', 'br', 'bs', 'bug', 'bxr', 'ca', 'cdo', 'ce', 'ceb', 'ch', 'chr', 'chy', 'ckb', 'co', 'crh', 'cs', 'csb', 'cu', 'cv', 'cy', 'da', 'diq', 'dsb', 'dty', 'dv', 'el', 'eml', 'en', 'eo', 'es', 'et', 'eu', 'ext', 'fa', 'ff', 'fi', 'fo', 'fr', 'frp', 'frr', 'fur', 'fy', 'ga', 'gag', 'gan', 'gd', 'gl', 'glk', 'gn', 'gom', 'gor', 'got', 'gu', 'gv', 'ha', 'hak', 'haw', 'he', 'hi', 'hr', 'hsb', 'ht', 'hu', 'hy', 'ia', 'id', 'ie', 'ig', 'ik', 'ilo', 'inh', 'io', 'is', 'it', 'iu', 'ja', 'jam', 'jbo', 'jv', 'ka', 'kaa', 'kab', 'kbp', 'ki', 'kk', 'kl', 'km', 'kn', 'ko', 'koi', 'krc', 'ks', 'ksh', 'ku', 'kw', 'ky', 'la', 'lad', 'lb', 'lbe', 'lez', 'lfn', 'lg', 'li', 'lij', 'lmo', 'ln', 'lo', 'lt', 'ltg', 'lv', 'mai', 'mdf', 'mg', 'mhr', 'mi', 'min', 'mk', 'ml', 'mn', 'mr', 'mrj', 'ms', 'mt', 'mwl', 'my', 'myv', 'mzn', 'na', 'nah', 'nap', 'nds', 'ne', 'new', 'ng', 'nl', 'nn', 'no', 'nov', 'nrm', 'nso', 'ny', 'oc', 'olo', 'or', 'os', 'pa', 'pag', 'pam', 'pap', 'pcd', 'pdc', 'pfl', 'pi', 'pih', 'pl', 'pms', 'pnb', 'pnt', 'ps', 'pt', 'qu', 'rm', 'rmy', 'ro', 'ru', 'rue', 'sa', 'sah', 'sat', 'sc', 'scn', 'sco', 'sd', 'se', 'sg', 'sh', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'srn', 'ss', 'stq', 'su', 'sv', 'sw', 'szl', 'ta', 'tcy', 'te', 'tet', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'tpi', 'tr', 'ts', 'tt', 'tw', 'ty', 'tyv', 'udm', 'ug', 'uk', 'ur', 'uz', 've', 'vec', 'vep', 'vi', 'vls', 'vo', 'wa', 'war', 'wo', 'wuu', 'xal', 'xh', 'xmf', 'yi', 'yo', 'za', 'zea', 'zh', 'zu']
