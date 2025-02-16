# Scraper for Polovni Automobili 

The idea is to create an automated file which would easily parse car's configuration, and place it into an  excel file.

This is a command line tool.

You can either create a new file, or save to an existing.

If a new file configuration is found, it will extend the existing file.

## How to use

To use you can either append to a file, or create a new.


```
python main.py --o testing --t excel --url 'https://www.polovniautomobili.com/auto-oglasi/25181599/volkswagen-golf-8-20dstyleled?attp=p1_pv0_pc1_pl1_plv0'

python main.py --a results/testing.xlsx --url 'https://www.polovniautomobili.com/auto-oglasi/25829255/volkswagen-golf-8-styleiqmasazamt6?attp=p1_pv0_pc1_pl1_plv0'
```

> Use main.py --h for more info.

## Todo

[] Add Contact info

[] Add a txt of links, go through all and spit out a result

[] Add a chronjob to scrape changes

[] Add a window tool to make life easier

[] Tool to show most highlight differences