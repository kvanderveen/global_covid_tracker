## Global COVID Tracker

A web-based application that utilizes the most recent 
global covid-19 data available from the Our World in Data 
[repository](https://github.com/owid/covid-19-data/tree/master/public/data).
The application allows one to explore global covid-19 data.
An example of the deployed application can be found
[here](https://global-covid-tracker.herokuapp.com). Shout out to 
the creators of [Streamlit](https://docs.streamlit.io) 
for making it easy to build a web application for data 
science.


### Quick start

* Clone the repo: ```git clone https://github.com/kvanderveen
/global_covid_tracker.git```
* cd into the directory: ```cd global_covid_tracker/```
* Install the requirements: ```pip install -r requirements.txt```
* Run the application: ```streamlit run app.py```

### What's included

Within the download you'll find the following directories and files.

```
global_covid_tracker
├── LICENSE
├── Procfile
├── README.md
├── app.py
├── global_covid_tracker
│   ├── __init__.py
│   ├── content
│   │   ├── __init__.py
│   │   ├── cases_content.py
│   │   ├── deaths_content.py
│   │   ├── growth_content.py
│   │   ├── introduction_content.py
│   │   └── testing_content.py
│   ├── dataframes
│   │   ├── __init__.py
│   │   ├── cases_dataframe.py
│   │   ├── deaths_dataframe.py
│   │   ├── growth_dataframe.py
│   │   ├── main_dataframe.py
│   │   └── tests_dataframe.py
│   ├── pages
│   │   ├── __init__.py
│   │   ├── cases.py
│   │   ├── deaths.py
│   │   ├── growth.py
│   │   ├── introduction.py
│   │   └── testing.py
│   ├── plotting
│   │   ├── __init__.py
│   │   ├── plot_cases_by_country.py
│   │   ├── plot_cases_growth.py
│   │   ├── plot_deaths_by_country.py
│   │   ├── plot_deaths_growth.py
│   │   ├── plot_positive_test_rates.py
│   │   ├── plot_total_cases.py
│   │   ├── plot_total_deaths.py
│   │   └── plot_total_tests.py
│   └── site_components
│       ├── __init__.py
│       ├── introduction_data.py
│       └── page_header.py
├── requirements.txt
└── setup.sh
```


### Creators
##### Kevin Vanderveen
* https://github.com/kvanderveen

