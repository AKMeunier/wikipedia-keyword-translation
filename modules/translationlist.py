import numpy as np
import pandas as pd
import os.path
import config
import shutil
import datetime
import re
import logging

class TranslationList():
    """
    Class to create keyword translation lists from wikipedia titles.
    """
    def __init__(self, lang1='de', lang2='en'):
        self.lang1 = lang1
        self.lang2 = lang2

    def create_titles_csv(self, dir_orig, dir_csv):
        """
        Creates a csv file from the original sql file, containing the page id and the title in language 1.
        (This is done by first creating several csv files with 300000 entries within a temp folder, and then combining them ito a single file.
        Otherwise there might be memory problems.)
        :param dir_orig: str, directory containing the original sql file
        :param dir_csv:  str, directory to save the csv file in
        :return: void
        """
        file_path = dir_orig + self.lang1 + "wiki-latest-page.sql"
        tempfolder = dir_csv + str(datetime.datetime.now().date()) +'-temp'

        if not os.path.exists(tempfolder):
            os.makedirs(tempfolder)
            logging.info('Created temp folder: %', tempfolder)

        if os.path.isfile(file_path):
            titles = open(file_path, 'r', encoding="utf8").read()
            logging.info('SQL file read: %', file_path)
            titles = titles[(titles.find("VALUES") + 8):]  # The entries we are interested in start 8 characters after the word "VALUES" in the sql file.
            titles_list = titles.split('),(')

            logging.info('Started creating % temp csv files.', int(np.ceil(len(titles_list) / 300000)))
            for i in range(int(np.ceil(len(titles_list) / 300000))):
                df_titles = pd.DataFrame()
                for line in titles_list[(i * 300000):min(((i + 1) * 300000), len(titles_list) + 1)]:
                    linesplit = line.split(',')
                    if linesplit[1] == '0':  # only titles of articles, not categories, authors etc.
                        df_titles = df_titles.append(pd.Series([int(linesplit[0]), linesplit[2][1:-1].lower().replace('_', ' ')]), ignore_index=True)
                df_titles = df_titles.rename(index=str, columns={0: 'page_id', 1: 'title_' + self.lang1})
                df_titles.to_csv(tempfolder + '/pages_' + self.lang1 + "_" + str(i + 1) + '.csv')
                logging.info('Finished % of %.', i+1, int(np.ceil(len(titles_list) / 300000)))

            logging.info('Started combining the temp csv files.')
            df_titles = pd.DataFrame()
            for i in range(int(np.ceil(len(titles_list) / 300000))):
                df_temp = pd.read_csv(tempfolder + '/pages_' + self.lang1 + "_" + str(i + 1) + '.csv', index_col=0)
                df_titles = df_titles.append(df_temp, ignore_index=True)
            df_titles = df_titles.reset_index(drop=True)
            df_titles.to_csv(dir_csv + '/pages_' + self.lang1 + '.csv')
            shutil.rmtree(tempfolder, ignore_errors=True)
            logging.info('Combined csv file finished, temp folder deleted.')

        else:
            print("No such file found. Download \'" + self.lang1 + "wiki-latest-page.sql\' from https://dumps.wikimedia.org/" + self.lang1 + "wiki/latest/.")

    def create_langlinks_csv(self, dir_orig, dir_csv):
        """
        Creates a csv file from the original sql file, containing the page id (language 1) and the title in language 2.
        (This is done by first creating several csv files with 300000 entries within a temp folder, and then combining them ito a single file.
        Otherwise there might be memory problems.)
        :param dir_orig: str, directory containing the original sql file
        :param dir_csv:  str, directory to save the csv file in
        :return: void
        """
        file_path = dir_orig + self.lang1 + "wiki-latest-langlinks.sql"
        tempfolder = dir_csv + str(datetime.datetime.now().date()) +'-temp'
        if not os.path.exists(tempfolder):
            os.makedirs(tempfolder)
            logging.info('Created temp folder: %', tempfolder)

        if os.path.isfile(file_path):
            langlinks = open(file_path, 'r', encoding="utf8").read()
            logging.info('SQL file read: %', file_path)
            # The entries we are interested in start 6 charaters before the first mention of the target language and continue until 7 characters before the first mention of
            # the alphabetically next language
            langlinks = langlinks[(langlinks.find(",'" + self.lang2 + "',")-6):(langlinks.find(",'" + config.langs[config.langs.index(self.lang2)+1] + "',") - 7)]
            langlinks_list = langlinks.split('),(')

            logging.info('Started creating % temp csv files.', int(np.ceil(len(langlinks_list) / 300000)))
            for i in range(int(np.ceil(len(langlinks_list) / 300000))):
                df_langlinks = pd.DataFrame()
                for line in langlinks_list[(i * 300000):min(((i + 1) * 300000), len(langlinks_list) + 1)]:
                    linesplit = line.split(',')
                    df_langlinks = df_langlinks.append(pd.Series([int(linesplit[0]), linesplit[2][1:-1].lower().replace('_', ' ')]), ignore_index=True)
                df_langlinks = df_langlinks.rename(index=str, columns={0: 'page_id', 1: 'title_' + self.lang2})
                df_langlinks.to_csv(tempfolder + '/langlinks_' + self.lang1 + "_" + self.lang2 + "_" + str(i + 1) + '.csv')
                logging.info('Finished % of %.', i+1, int(np.ceil(len(langlinks_list) / 300000)))

            logging.info('Started combining the temp csv files.')
            df_langlinks = pd.DataFrame()
            for i in range(int(np.ceil(len(langlinks_list) / 300000))):
                df_temp = pd.read_csv(tempfolder + '/langlinks_' + self.lang1 + "_" + self.lang2 + "_" + str(i + 1) + '.csv', index_col=0)
                df_langlinks = df_langlinks.append(df_temp, ignore_index=True)
            df_langlinks = df_langlinks.reset_index(drop=True)
            df_langlinks.to_csv(dir_csv + '/langlinks_' + self.lang1 + "_" + self.lang2 + '.csv')
            shutil.rmtree(tempfolder, ignore_errors=True)
            logging.info('Combined csv file finished, temp folder deleted.')

        else:
            print("No such file found. Download \'" + self.lang1 + "wiki-latest-langlinks.sql\' from https://dumps.wikimedia.org/" + self.lang1 + "wiki/latest/.")

    def create_translations(self, df_titles, df_langlinks, exclude_same=True, intersect=None, intersect_exact=True):
        """
        Creates a translation list from the
        :param df_titles: Pandas DataFrame, contains the page id and titles of language 1
        :param df_langlinks: Pandas DataFrame, contains the page id of language 1 and the translated titles of language 2
        :param exclude_same: bool, if true, all entries of the translation data frame which are the same in both languages are deleted
        :param intersect: list, contains a list of keywords, that will be intersected with df_langlinks.
        :param intersect_exact: bool, if true, only exact matches in the intersection of df_langlinks and intersect are considered. If false, all entries that contain the specified
        keyword are considered (e.g. for keyword "neural network" also "artificial neural network" is included.)
        :return: Pandas DataFrame
        """
        if intersect is not None:
            if intersect_exact:
                df_langlinks = df_langlinks[df_langlinks["title_" + self.lang2].isin(intersect)]
            else:
                select_final = set()
                for keyword in intersect:
                    pattern = re.compile(".*" + keyword + ".*")
                    select_kw = set()
                    i = 0
                    for title in list(df_langlinks["title_" + self.lang2]):
                        if pattern.search(str(title)):
                            select_kw.add(i)
                        i += 1
                    select_final = select_final.union(select_kw)
                df_langlinks = df_langlinks.iloc[sorted(list(select_final)), ]

        df_translations = df_titles.merge(df_langlinks, how='inner', on='page_id')
        df_translations = df_translations.rename(index=str, columns={'title_' + self.lang1: 'keyword_' + self.lang1, 'title_' + self.lang2: 'translation_' + self.lang2})
        df_translations = df_translations.drop('page_id', axis=1)
        df_translations = df_translations.dropna()

        if exclude_same:
            df_translations = df_translations[df_translations['keyword_' + self.lang1] != df_translations['translation_' + self.lang2]]

        return df_translations





