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
## Cleaning
- The CSV are transferred into a DataFrame (DF)
- The DF is checked for illegal data. 
    - The discovery function is found in `funtions/discovery.py`
    - The configuration options for these functions are found in `data/config.py`
- The DF is cleaned from illegal data. The cleaning actions can be found at `functions/clean.py`
- The datatypes of the DF's columns are matched to their content. These functions can be found in `functions/transform.py`

## Regression and Prediction
The model predicts the house prices with 3" different type of regression, these being:
- Linear regression
- ElastiNet regression
- Lasso regression
- Ridge regression

# Bugs

**Q:** The discover function says that there are still illegal values in `MasVnrType`, `BsmtQual` and `GarageType`.<br>
**A:** This is because, for the regression function to work, some values need to be altered that aren't considered validated by the config file that `discover` uses. These are mainly `NaN` files that are re-assigned a string value.

**Q:** Some code in the transform function is in comment.<br>
**A:** This was, because originally, there was decided to transform data within the dataset to the right dataset. But when transforming date data in the dataset, it doesn't play nicely with regression calculation. Because of this, we've decided to not do that.

# FAQ
**Q:** Where are `test.csv` and `train.csv`? <br>
**A:** We personally found that these naming was very confusing, so we've decided to rename the datasets:
- `train.csv` -> `dataset_with_sale.csv`
- `test.csv` -> `dataset_without_sale.csv`