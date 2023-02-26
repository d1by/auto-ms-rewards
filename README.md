# Auto Microsoft Rewards

automatically claims maximum number of daily points achievable

## Description

Input: 
* number of searches (varies with Microsoft Rewards Level - default: 10)
* path to Edge User Data folder
 
Output:
* performs searches on Bing using Microsoft Edge
* clears searches from browser history 

## Getting Started

### Dependencies
* Microsoft Edge
* Python (tested on 3.10.7)
* Selenium (tested on 4.8.2)

To check your versions, run the following in a command prompt:
```
python --version
```
```
python -c "import selenium; print(selenium.__version__)"
```

### Installing
* Download Microsoft Edge, if not already installed
* Sign into Microsoft Edge with your account
* Download python: https://www.python.org/downloads/
* Install Selenium:
   * Type the following in a command prompt:
      ```
      pip install selenium
      ```

### Executing program

* Find your Edge User Data folder:
 * Default: 
       ```
       C:\Users\<Name>\AppData\Local\Microsoft\Edge\User Data
       ```
 * If your Microsoft Edge is installed elsewhere, open Edge and go to edge://versions -> Profile Path -> Copy everything just and before ```\Profile X```
 * Replace file path in auto-ms-rewards.py
* Edit number of searches, if it is different from the default (10)

## Troubleshooting

#### Edge opens, but bing.com doesn't load:
 * end the Microsoft Edge task in task manager
 * run again
 * if the problem persists, restart your system
 
 This error occurred multiple times during testing, and restarting the system fixed it 100% of the time
 Cause has not been determined

## Authors

Diby M.  
Discord: diby#9420   
[Discord Server](https://discord.gg/frErDjHStx)

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [Selenium with Python - Read the Docs](https://selenium-python.readthedocs.io/)
