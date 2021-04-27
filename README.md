![Logo](documentation/Logo.png)

---

# Introduction

Welcome to the BDPG-1 project! This project is a group project by 
- Bo Robbrecht ([@BT-Creator](https://github.com/BT-Creator))
- Lennert Commeine([@lennert05](https://github.com/lennert05))
- Steffen Gemin([@steffen-gemin](https://github.com/steffen-gemin))
- Benjamin Robbe([@benjaminrobbe](https://github.com/benjaminrobbe))

This project uses the Ames Housing Set in order to predict sell prices of houses.

# Dashboards
In order to visualize data, we've used **Tableau**. The Tableau data can be found in the `tableau` directory.

# Machine Learning
The ML model is written within Python and performs multiple actions:
- The CSV are transferred into a DataFrame (DF)
- The DF is checked for illegal data. 
    - The discovery function is found in `funtions/discovery.py`
    - The configuration options for these functions are found in `data/config.py`
- The DF is cleaned from illegal data. The cleaning actions can be found at `functions/clean.py`
- The datatypes of the DF's columns are matched to their content. These functions can be found in `functions/transform.py`


