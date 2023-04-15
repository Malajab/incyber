@echo off
set "OutputFile=%USERPROFILE%\Desktop\ScheduledTasks.csv"
powershell.exe -Command "Get-ScheduledTask | Select-Object TaskName, TaskPath, State, LastRunTime, NextRunTime | Export-Csv -Path '%OutputFile%' -NoTypeInformation"
