Windows  
- Download Python3 (version 3.7) at https://www.python.org/downloads/ [Windows x86-64 executable installer]
- add python to your PATH 
    - Windows -> Run ("Ausf�hren") -> "sysdm.cpl"
    - Advanced -> Environment Variables
    - System Variables "Edit" 
    - Add the installation path, something like "C:\Users\Jan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7"
 - open up a terminal and type "python" to check if everything worked
 
 - install "git": https://git-scm.com/download/win
 - download/clone this project: ``git clone https://github.com/kono94/covid-analysis.git``
 - get into the folder ``cd covid-analysis``
 - create a virtual environment ``python -m venv env``
 - enter the environment ``env\Scripts\activate.bat``
 - "(env)" should appear at the beginning of the terminal line
 - install needed dependencies with command ``pip install -r requirements.txt``
 - run the test script ``python covidStats.py``
 - a browser window should open and a pie chart! 