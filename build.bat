rd /q /s %cd%\dist
rd /p /s %cd%\build
pyinstaller --version-file=file_version_info.txt --icon=randomCall.ico -w randomCall.py
copy %cd%\randomCall.ico %cd%\dist\randomCall\randomCall.ico