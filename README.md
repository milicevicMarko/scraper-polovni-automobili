# Scraper for Polovni Automobili 

The idea is to create an automated file which would easily parse car's configuration, and place it into an  excel file.

This is a command line tool.

You can either create a new file, or save to an existing.

If a new file configuration is found, it will extend the existing file.

## How to use

Two modes of usage: **by Batch** or **by URL**.

In both versions you need to pass a path to the file you wish to update/create. 
The Files it can read are `XLSX, XLS, JSON, CSV`.

- If the file exists, it will be extended and saved to `results/<file_name>.<file_type>`
- If the file does not exits, it will be created at the same `results/<file_name>.<file_type>`

> Use main.py --h for more info.

### Batch
```
python main.py --file "results/result.xlsx" --batch "batch.txt" 
```

> Expects a TXT file with a list of URLs split by a space/newline.


### Single URL
```
python main.py --file "results/result.xlsx" -- url "https://www.polovniautomobili.com/auto-oglasi/25181599/volkswagen-golf-8-20dstyleled?attp=p1_pv0_pc1_pl1_plv0"
```

# Visualize

In order to visualize, you need to run:

`streamlit run visualize.py -- <path_to_your_file>`

> It can be xlsx, csv, json.

## Todo

[] Add Contact info

[] Add a chronjob to scrape changes

[] Add a window tool to make life easier for importing files

[] Tool to show most highlight differences