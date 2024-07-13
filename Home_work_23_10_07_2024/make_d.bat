@ECHO OFF

set "folderPath=.\venv"

set setActivate=%1

echo %setActivate%

if not exist %folderPath% (
    python -m venv venv
) else (
    echo "Folder is present"
    call vaa.bat
    python -m pip install -U pip
    pip install python_docx auto-py-to-exe
    pip list
    auto-py-to-exe text_input.py
    cd ./output/text_input/
    text_input.exe
)
    
    