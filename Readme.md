## The Zebra Project: UI Acceptance Test Assessment

#### Project

The project was created in PyCharm, MacOS

Executed with chromedriver: 83.0.4103.39 and GoogleChrome: 83.0.4103.116

Supports Firefox and Safari 

#### Setup environment

- Install required packages:

```shell script
python3 setup.py install
```

### Driver verification

The testing was done using chromedriver

Download: https://chromedriver.chromium.org/downloads

MacOs install: 
 
```shell script
$ brew cask install chromedriver
$ chromedriver --version
```

#### Execute tests

 - to execute all tests
```shell script
behave --format=plain --show-timings
```
- to execute tests from a specific feature
```shell script
behave features/user_flow.feature --format=pretty --show-timings
```

#### Debug issues with chromedriver

See https://stackoverflow.com/questions/48513369/cant-update-chromedriver-in-macos10-12-6
