# osd_count_profiles
Plot histograms of the annual counts of CTD, BOT and CHE profiles from the Ocean Sciences Division using Python.

There are two steps to producing the plots.
1. All files containing profile data in the archive contain one file only, so the first step is to count all file types in the archive and save these numbers in a csv file. This step uses *get_ctd_bot_profile_counts.py*.
2. Plot the counts from the csv file using *hist_osd_profile_counts.py*.
