# puc testing:


## Selenium Test

### Installation:


#### Install Python and Browsers:

Use FROM circleci/python:3.7.0a2-browsers if you want to run in circleci 

or... 

Download and install Python 3.7

Download and install Chrome

Add to PYTHONPATH path_to_repo  to use it locally

#### Install Behave -> BDD test, allure behave -> formatter for test results:
```
sudo pip install behave
pip install allure-behave
```
#### Install test dependencies:
```
pip install regex
pip install arrow
pip install nose
```
#### Install selenium and Chromedriver -> controlling browser: 
```
sudo pip install selenium
sudo pip install chromedriver
sudo pip install chromedriver-binary
```
#### Install allure-> generate reports on the machine: 
```
git clone https://github.com/Linuxbrew/brew.git ~/.linuxbrew
PATH="$HOME/.linuxbrew/bin:$PATH"
export MANPATH="$(brew --prefix)/share/man:$MANPATH"
export INFOPATH="$(brew --prefix)/share/info:$INFOPATH"            
brew install allure
```

#### Create path for screenshots:
```
mkdir puc_testing/Screenshots/features
mkdir puc_testing/Screenshots/


### Running tests:
This test harness is quite versatile, allowing the use of flags to control which set of tests you want to run and which
variants of execution as environments, enabling screenshots and headless browsers, 
if an option is omitted, the default value is taken 


run behave -D screen_capture=no
```
to be able to run headless or launching browsers, options yes or no, default no:
```
run behave -D headless=yes/no
```
to be able to run a subset of test use tags, it is possible to combine and exclude tags:
```
behave --tags=smoke --no-skipped
```
to be able to generate junit xlm file with the result:
```           
behave  --junit --junit-directory 
```
full command line example to test selenium with allure formatter:
```
behave --tags=ui --tags=regression -D screen_capture=yes -D headless=no -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features --junit --junit-directory ./allure_result_folder 
```
full command line example to test Rest with allure formatter:  
```  
behave --tags=services --tags=regression -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features --junit --junit-directory ./allure_result_folder   
```  

### Generate allure html reports:
for html reports:
```
allure generate /path_to/allure_result_folder/ -o /path_to_web_results/web/

```

for server reports:
``` 
allure serve path_to_reesult_folder
``` 

## Documentation

### About Behave

http://pythonhosted.org/behave/tutorial.html#features

### About Selenium WebDriver

http://selenium-python.readthedocs.io/getting-started.html




