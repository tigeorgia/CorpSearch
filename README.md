This is a Django app built to provide an interface to data downloaded from the 
Georgian [Public Registry website by](https://enreg.reestri.gov.ge) by [TI Georgia's scraper](https://github.com/tigeorgia/GeorgiaCorporationScraper).

Installation
==============
1. `virtualenv corp_search`
2. `cd corp_search`
3. `source bin/activate && git clone https://github.com/tigeorgia/CorpSearch.git`
4. `cd CorpSearch && pip install -r requirements.txt`
5. `cp settings.py.example settings.py` and edit to suit.
6. `manage.py syncdb`
7. `manage.py migrate corporations`
8. `manage.py migrate person`

Loading Data
=================
You'll need to populate the database using data from the scraper mentioned above.
This data is stored in JSON files; there are three JSON files that are currently used:
* Corporation.json
* PersonCorpRelation.json
* RegistryExtract.json

The functions to load data from these files into the database are located in
apps/corporations/load and apps/person/load, but there is unfortunately no
completely automated load script yet.

You will need to open up a Django shell using `manage.py shell` and then import
the data files manually using the functions in these files:
* Corporation.json -> apps/corporations/load/corporations.py
* PersonCorpRelation.json -> apps/person/load/people.py
* RegistryExtract.json -> apps/corporations/load/extracts.py

**Important:** You MUST load the data in the following order:
1. Corporations
2. People (from PersonCorpRelation.json)
3. Affiliations (from PersonCorpRelation.json)
4. Extracts (from RegistryExtract.json)
