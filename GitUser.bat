@echo off

if not exist %~dp0GitUser.py goto no_script
call python3 %~dp0GitUser.py %*

::That's it !
goto :EOF

:no_script
echo Warning: GitUser.py script not found
   