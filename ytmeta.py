import pandas as pd
from youtube_extract import __main__ as ydl

wildcat = ydl.extract_entries_for_url('https://www.youtube.com/c/3ildcat')
wildcat_series = pd.Series(wildcat)
wildcat_series.to_csv(r'/Users/deb/Desktop/youtube/wildcat.csv', header = True)
