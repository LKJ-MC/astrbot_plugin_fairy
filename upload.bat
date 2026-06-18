@echo off
chcp 65001 >nul
git add .
git commit -m "更新于 %date% %time%"
git push origin master
pause