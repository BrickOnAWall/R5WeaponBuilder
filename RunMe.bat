@echo off
setlocal enabledelayedexpansion

set /p input=Skip Install? Y/N: 

if /i "!input!"=="N" (
    pip install -r requirements.txt
)

python drawUI.py

endlocal
