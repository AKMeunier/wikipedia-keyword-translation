
def create_lang_list(filename, directory):
    """
    Creates a list of all available languages in a given wikipedia langlinks file.
    :param filename: str, example: "dewiki-latest-langlinks.sql
    :param directory: str, path to the file example: "data/downloads/"
    :return: list
    """
    langs = []
    langlist = open(directory + filename, 'r', encoding="utf8").read()

    for i in range(300):
        langlist = langlist[(langlist.find("\'),(843020,\'") + 18):]  # entry for wikipedia page, should exist in every language
        language = langlist[(langlist.find(",\'")+2):(langlist.find("\',\'"))]
        langs.append(language)

    sorted(list(set(langs)))

    langs2 = [s for s in langs if len(s) >= 2 and len(s) <= 3]

    return langs2