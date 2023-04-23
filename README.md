---
---
### ***DISCLAIMER***

https://promos.microsoftrewards.com/US/en/MS_PB_APR_INT_21/rules
# ***"Use of any automated system to participate is prohibited and will result in disqualification."***

### ***This is for educational purposes only, and was created solely to test the capabilities of Selenium. I do not condone the use of this script in any real world situation.***
---
---

# Auto Microsoft Rewards

automatically claims maximum number of daily points achievable



## Description

Input: 
* number of searches (varies with Microsoft Rewards Level - default: 10)
* path to Edge User Data folder
 
Output:
* scrapes bing.com home page for news article links
* performs searches on Bing using Microsoft Edge
* clears only these searches from browser history 

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
 * Default: ```C:\Users\<Name>\AppData\Local\Microsoft\Edge\User Data```
   * If this path exists, then you don't have to change anything
 * If your Microsoft Edge is installed elsewhere, open Edge and go to edge://versions -> Profile Path -> Copy everything just before ```\Profile X```
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

* 2.0
    * now scrapes bing.com home page for news article links, and uses this to perform searches 

* 1.0
    * Initial Release

## License

This project is licensed under the [MIT](https://github.com/d1by/auto-ms-rewards/blob/6a0bbfe8c13ecc194c1bdafa27c86ce8c00dad7c/LICENSE) License - see the LICENSE.md file for details

## Acknowledgments

* [Selenium with Python - Read the Docs](https://selenium-python.readthedocs.io/)
