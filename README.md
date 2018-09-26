# Introduction
With this project, you can extract translations of keywords from wikipedia titles. 

# Folder structure
```
wikipedia-keyword-translation
├── data
│   ├── downloads                   # for original sql files from wikipedia dump
│   ├── lists                       # for csvs created from the sql files
├── modules
│   ├── translationlist.py          # class to create the translation list
│   ├── utils.py                    # useful functions
├── config.py                       # settings
├── main.py                         # run to create translation list
├── README.md
├── requirements.txt
```

# Module description

`translationlist.py`      
Class for translation list creation

`utils.py`     
Useful functions

# The data
* Create the folder `data` at project top-level. Within, create the two folders `downloads` and `lists`. (If you want a different folder structure, change the respective paths in `config.py`)
* If you have access to processed csv files, put these into the `lists` folder.
* If you don't have access to the csv files:
    * Download `dewiki-latest-page.sql` and `dewiki-latest-langlinks.sql` from https://dumps.wikimedia.org/dewiki/latest/ (For other languages, change the *de* to something else, e.g. *en*.)
    * Put these files into the `downloads` folder
    
# How to create a translation list
* If necessary, make changes to the settings in `config .py`:
    * Languages
    * List of keywords to intersect translation list with (`list_intersect`). If this is not `None`, the target language entry column of the final translation list wll only contain keywords that are in `list_intersect`.
    * If you are intersecting, whether the matches should be exact or not. (If not, all entries containing one of the keywords are included, e.g. if "neural network" is in the list, also "artificial neural network" will appear in the translation list)
* If the csv data is not available, uncomment the upper part in order to create csv files from the sql files.
* Run `main.py`.

