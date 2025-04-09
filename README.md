install python then check if python was install with:

python --version

Then install all extra libraries for the program to run with:

pip install pywin32 json

Ensure pywin32 is properly Set Up with:

python -m pywin32_postinstall

if pywin32 or pip are not recognized, try:

pip install --force-reinstall pywin32
python -m ensurepip --default-pip

To run the program go to the directory where the program was download example:

cd /Desktop\Bot-For-Alex-main

Then run the program with:

python Bot.py
