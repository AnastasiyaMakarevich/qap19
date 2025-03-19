# __Autotests for 21vek website__
***
## __Overview__
***
This repository contains a comprehensive suite of automated tests for the 21vek website.
The project contains UI-tests. The project can be launched in the Chrome browser. The design pattern of this project is Page Object Model and contains the following:

* python package that contains the files with base url and assertions
* python package with locators for pages
* python package with pages (base_page, main_page, basket_page, favorites_page, account_page)
* package test which contains tests for each page
* conftest - file with project settings (pytest fixtures for driver)
* README file with information about the project
***
## Installation Guide
***
### Prerequisites:
Ensure you have Python 3.12 installed.
#### Setup Instructions:
1. Clone the repository:
```
git clone https://github.com/AnastasiyaMakarevich/qap19/diplom
cd diplom
```
2. Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```
3. Install required dependencies:
```
pip install -r requirements.txt
```
4.  Running tests
```
make test_all
```
***
Author: Anastasiya Makarevich
GitHub: github.com/AnastasiyaMakarevich
***

