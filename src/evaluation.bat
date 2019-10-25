@echo off
set root_path=/mnt/c/Users/Milano/Desktop/wind-turbine_design_optimization
set python_path=%root_path%/EC2019/jpnsecCompetition2019/bin/python
set eval_script=%root_path%/evaluation/windturbine_SOP.py
set dir_path=%root_path%/evaluation

wsl %python_path% %eval_script% %dir_path%