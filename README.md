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
9. Download [Blueprint](http://blueprintcss.org/) and install it into static/css if you care how things look.

Loading Data
=================
You'll need to populate the database using data from the scraper mentioned above.
This data is stored in JSON files; there are three JSON files that are currently used:
* Corporation.json
* PersonCorpRelation.json
* RegistryExtract.json

In order to load data, management commands have been created (in the util app).
To load data for the first time, AFTER you've run syncdb and migrate in the 
installation instructions, copy the three files above into a folder called 
"data" in the same directory as this README file.

Next, issue (in this order):

1. `manage.py loadcorps`
2. `manage.py loadpeople`

And then sit back and wait, because it'll take a while.

If you need to reload the data for some reason (e.g. to load a new scrape), just
issue: `manage.py resetcorps` or `manage.py resetpeople`.

The commands have been optimized to balance speed and memory usage; you
shouldn't have a problem on most modern machines.

Scripts
===========
There are some helpful utility scripts for updating the site (assuming you use
PostgreSQL) in the scripts folder. They use the [Fabric](http://docs.fabfile.org/en/1.6/) library.
You'll need to write your own fabfile.py importing the modules in scripts. That
file is deliberately missing from this repository in order to avoid exposing
server configuration details.


License
=======

Company Info is released under the terms of [GNU General Public License (V2)](http://www.gnu.org/licenses/gpl-2.0.html).
