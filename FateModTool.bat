@echo off
title Fate Cache Remover Tool
color 1
echo ===================================================================
echo Fate Cache Remover Tool
echo v1.0
echo ===================================================================
echo Make Sure Cache Is The Correct Directory
echo -------------------------------------------------------------------
:loop
echo ....................................................Delete Cache?
del C:\ProgramData\WildTangent\FateSteam\Cache
rmdir /S /Q "C:\ProgramData\WildTangent\FateSteam\Cache"
mkdir C:\ProgramData\WildTangent\FateSteam\Cache
echo ..........................................................Removed
pause
goto loop
