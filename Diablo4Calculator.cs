@echo off
:loop
set /p "num=Enter Character Level: "
set /a "result=num-43"
set /a "monsterlevel=num+10"
cls
echo Level:%num%
echo Tier:%result%
echo Monster Level:%monsterlevel%
echo BonusLevel +10: 15% XP
goto loop
// .bat file that lets the user know what nightmare dungeon tier they need to play at for maxinum XP bonus
