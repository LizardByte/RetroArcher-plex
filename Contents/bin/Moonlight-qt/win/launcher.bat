@echo off
set clientIP=%1
set moonlightPcUuid=%2
set moonlightAppName=%3
set u=%4
set p=%5

schtasks /create /TN "\RetroArcher launcher" /s "%clientIP%" /sc onlogon /tr "C:\Program Files\Moonlight Game Streaming\Moonlight.exe stream %moonlightPcUuid% %moonlightAppName%" /f /u "%u%" /p "%p%"
schtasks /run /TN "\RetroArcher launcher" /s "%clientIP%" /u "%u%" /p "%p%"
schtasks /delete /TN "\RetroArcher launcher" /s "%clientIP%" /u "%u%" /p "%p%" /f
