import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


def do_hist_profile_counts(time, counts, output_name,
                           instrument, barcol):
    # Adjust the start year
    # to account for no CTD data before 1950
    start_idx = 0
    profile_count = counts[start_idx]
    while profile_count == 0:
        start_idx += 1
        profile_count = counts[start_idx]

    # plt.hist(time, bins=num_bins, align='left',
    #          c=barcol, alpha=0.5)
    barwidth = 1.
    plt.bar(time[start_idx:], counts[start_idx:],
            align='edge', width=barwidth, color=barcol,
            edgecolor=barcol, alpha=1)
    # plt.stairs(counts[start_idx:], time[start_idx-1:],
    #            fill=True, color=barcol)
    # plt.step(counts[start_idx:], time[start_idx:],
    #            fill=True, color=barcol)

    # Add gridlines
    plt.grid(color='lightgrey')
    plt.ylabel(f'Num of {instrument} Profiles')
    plt.tight_layout()
    plt.savefig(output_name)
    plt.close()
    return


parent_dir = 'C:\\Users\\HourstonH\\Documents\\ctd_bot_profile_counts\\'
input_file = os.path.join(
    parent_dir, 'osd_archive_profile_counts_sept29.csv')

df = pd.read_csv(input_file)

# Make bottle and che histogram
# alpha controls the opacity
png_bot = os.path.join(
    parent_dir, 'osd_bot_profile_counts_per_year.png')

do_hist_profile_counts(
    df.loc[:, 'Year'],
    df.loc[:, 'BOT'] + df.loc[:, 'CHE'],
    png_bot, 'BOT', barcol='tomato')

# Make ctd histogram
png_ctd = os.path.join(
    parent_dir, 'osd_ctd_profile_counts_per_year.png')

do_hist_profile_counts(
    df.loc[:, 'Year'],
    df.loc[:, 'CTD'],
    png_ctd, 'CTD', barcol='royalblue')
