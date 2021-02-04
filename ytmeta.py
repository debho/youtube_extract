import pandas as pd
from youtube_extract import __main__ as ydl

# INSTRUCTIONS

## enter the url to extract data from
# channel_name = ydl.extract_entries_for_url('enter url as a string')

## convert from list to series
# channel_name_series = pd.Series(channel_name)

## writes to CSV
# channel_name_series.to_csv(r'(path name, so yours would probably be something like /Users/Samantha/Desktop/(folder name)/filename.csv)', header = True)
# header = True makes sure that the first row of data is included in the table, otherwise it'll just make the first row of data the header and that is not stonks

## SAMPLE CODE THAT I COMMENTED OUT FOR REF
# smiletoys = ydl.extract_entries_for_url('https://www.youtube.com/channel/UCjZ-Ekz7JDN6GDXwusvSHvg/videos?view=0&sort=p&flow=grid')
# smiletoys_series = pd.Series(smiletoys)
# smiletoys_series.to_csv(r'/Users/deb/Desktop/youtube/smiletoys.csv', header = True)











