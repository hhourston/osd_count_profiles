import os
import glob
import numpy as np
import pandas as pd
from tqdm import trange

"""
Plot histograms showing the annual profile count
for CTD and BOT data in the OSD Data archive. Use
the USB copy of the OSD Data Archive instead of
downloading all the data.
"""

# parent_dir = '/usb/OSD_Data_Archive/Cruise_Data/'
parent_dir = 'Y:\\Cruise_Data\\'

# 1930 is the first year of cruises in the data archive
years = np.arange(1930, 2022+1, dtype='int32')

# Initialize dataframe to hold profile counts
df_counts = pd.DataFrame(
    {'Year': years,
     'BOT': np.zeros(len(years)),
     'CTD': np.zeros(len(years)),
     'CHE': np.zeros(len(years))}
)
df_counts.set_index('Year', inplace=True)

# # OSD_Data_Archive
# parent_dir = 'Y:\\'
# l1 = glob.glob(parent_dir + '**\\*1930*.bot*', recursive=True)
# l2 = glob.glob(parent_dir + '**\\*1930*.bot', recursive=True)
# l2 = glob.glob(parent_dir + '**\\*1930*.bot.nc', recursive=True)

for i in trange(len(years)):
    y = years[i]
    # Subdirectory structure is /year/cruise-number/Bottle/*.bot
    # or /year/cruise-number/BOTTLE/*.bot
    # *.bot searches both *.bot and *.BOT files, if the latter
    # exist
    df_counts.loc[y, 'BOT'] += len(
        glob.glob(
            parent_dir + f'{y}/*/*/*.bot', recursive=True))
    df_counts.loc[y, 'CTD'] += len(
        glob.glob(
            parent_dir + f'{y}/*/*/*.ctd', recursive=True))
    df_counts.loc[y, 'CHE'] += len(
        glob.glob(
            parent_dir + f'{y}/*/*/*.che', recursive=True))

print(df_counts)

# Export the counts in a file
# output_dir = '/home/hourstonh/Documents/osd_profile_counts/'
output_dir = 'C:\\Users\\HourstonH\\Documents\\ctd_bot_profile_counts\\'
output_file = os.path.join(
    output_dir, 'osd_archive_profile_counts_sept29.csv')

# Keep index as it is
df_counts.to_csv(output_file)
