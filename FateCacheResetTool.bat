@echo off
title Fate Cache Reset Tool
color 1
echo ===================================================================
echo Fate Cache Reset Tool
echo v1.0
echo ===================================================================
echo Make Sure Cache Is The Correct Directory
echo -------------------------------------------------------------------
:loop
echo .....................................................Reset Cache?
del C:\ProgramData\WildTangent\FateSteam\Cache
rmdir /S /Q "C:\ProgramData\WildTangent\FateSteam\Cache"
mkdir C:\ProgramData\WildTangent\FateSteam\Cache
echo ..........................................................Removed
pause
goto loop
