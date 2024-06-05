#!/bin/zsh

# Activate the virtual environment
source /Users/koushikmahanta/Desktop/ProjectSimulation/bin/activate

# Execute the Python scripts in order
python compare.py
python plot_user_vs_power.py
python plot_height_vs_power.py
python plot_height_vs_avg_channelgain.py

# Deactivate the virtual environment
deactivate
