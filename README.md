# misbehavin

A ragime problem causer. 


To install,

    python setup.py develop


Also - separately, install weave.


## Web Integration


Download the web driver for your system: https://github.com/mozilla/geckodriver/releases


then:

    export RAGTIME_WEB_DRIVER_PATH=/Users/victor/Downloads/geckodriver


## Components

### Planner

To see the test plan for a website based on the description, call:

    misbehavin_planner "A chocolate shop"
    misbehavin_chatter 'A chocolate shop' 'Get a recommendation.'


  