from modules.translationlist import TranslationList
import config
import pandas as pd
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

# Instantiate with two languages (the first one should be the one you are translating from)
tl = TranslationList(config.lang1, config.lang2)

# Create csvs from the original sql data. run this over night, or use available csvs instead.
#tl.create_titles_csv(config.dir_original, config.dir_titles)
#tl.create_langlinks_csv(config.dir_original, config.dir_langlinks)

# Read in the csvs
df_titles = pd.read_csv(config.dir_titles + "pages_de.csv", index_col=0)
df_langlinks = pd.read_csv(config.dir_langlinks + "langlinks_de_en.csv", index_col=0)

# Create the df of translations, optionally intersected with some other list
# Set intersect_exact to True, if only exact matches are to be found. Else all entries that contain one of the given keywords are included.
df_translations = tl.create_translations(df_titles, df_langlinks, intersect=config.list_intersect, intersect_exact=config.intersect_exact)

# Save the translation
df_translations.to_csv(config.dir_final + '{}_translations_{}_{}.csv'.format(str(datetime.datetime.now().date()), config.lang1, config.lang2))

print(df_translations)

