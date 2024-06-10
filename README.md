# Subleva Project Repo for DoC 2024 

# Project Overview

This is our project repository for Subleva: A Migration analytics app for our final project developed for the Summer 2024 DoC in Leuven, Belgium titled Data and Software in International Government and Politics.

Currently, there are three major components:
- Streamlit App (in the `./app` directory)
- Flask REST api (in the `./api` directory)
- SQL setup files (in the `./database` directory)

## About
Subleva aims to mitigate this contention by providing a quantitative approach to understanding migration from both perspectives and offers resources for migrants.

## How to Set Up and Run
To use Subleva, select the user persona that you would like to act as, and use the side bar links to navigate to and from pages. Once you are done with the user persona, please select the Log Out button at the bottom left of the side bar. 

## Deployment

To deploy this project run

```bash
  docker compose up -d
```
to activate the (in the `./app` directory), (in the `./api` directory), (in the `./database` directory). 

Once the containers are started and properly running, please click on the link witin the front-end, which is hosted at 

```bash
    http://localhost:8501/
```

## API Notes
Subleva uses large scale data that might take a while to process, so please give it a while to process and load! 

## Authors
This project consisted of work and collaboration from Carson Hunter, Ivionna Jordan, and Dylan Sacks. Here are our other project repositrories and works below: 

- [@jordan-iv](https://www.github.com/jordan-iv)
- [@carson-hunter5](https://github.com/carson-hunter5)
- [@dylansacks](https://www.github.com/dylansacks)

## Acknowledgements
 - [Mark Fontenot's Summer DoC Project Template](https://github.com/NEU-Khoury-DoC/24su-doc-template)