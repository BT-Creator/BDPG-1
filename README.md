![Logo](documentation/Logo.png)

---

# Introduction

Welcome to the BDPG-1 project! This project is a group project by

- Bo Robbrecht ([@BT-Creator](https://github.com/BT-Creator))
- Lennert Commeine([@lennert05](https://github.com/lennert05))
- Steffen Gemin([@steffen-gemin](https://github.com/steffen-gemin))
- Benjamin Robbe([@benjaminrobbe](https://github.com/benjaminrobbe))

This project uses the Ames Housing Set in order to predict sell prices of houses.

# Quick Start Guide
1. Git clone the project
2. At the root file, make a directory with the following structure:
  ```
  .
  └── export
      ├── elasticNet
      ├── lasso
      ├── linear
      └── ridge
  ```
3. Run the `main.py` script. It will generate all the possible combinations of models we've researched. 
   If you want to disable some aspect of the project, you can comment out the prediction in the prediction dictionaries.

# Data Visualization

In order to visualize data, we've used **Tableau**. The Tableau data can be found in the `tableau` directory.

# Machine Learning

The ML model is written within Python and performs multiple actions:

## Cleaning

- The CSV are transferred into a DataFrame (DF)
- The DF is checked for illegal data.
    - The discovery function is found in `funtions/discovery.py`
    - The configuration options for these functions are found in `data/config.py`
- The DF is cleaned from illegal data. The cleaning actions can be found at `functions/clean.py`
- The datatypes of the DF's columns are matched to their content. These functions can be found
  in `functions/transform.py`

## Regression and Prediction

### Pre-modification

The data first goes through a preparation fase, where:

- All numerical data is normalized
- All non-filled categorical data is filled with dummies and then numerated.
- All missing possibilities are added to both dataset

### Models & Predictions

The model predicts the house prices with 4 different type of regression, these being:

- Linear regression
- ElastiNet regression
- Lasso regression
- Ridge regression

At the current time of writing is **Lasso Regression with Pearson Optimization** the most optimal model, with a 0,20600
score on [kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/leaderboard) *(Lower is better)*.

# FAQ

**Q:** Where are `test.csv` and `train.csv`? <br>
**A:** We personally found that these naming was very confusing, so we've decided to rename the datasets:

- `train.csv` -> `dataset_with_sale.csv`
- `test.csv` -> `dataset_without_sale.csv`

**Q:** When making the export files, the program returns that it's unable to find the file.<br>
**A:** In order to export the file, you'll need to create the directories in order to export these at the root of the
project. This should look like this:

```
.
└── export
    ├── elasticNet
    ├── lasso
    ├── linear
    └── ridge
```

**Q:** Why the name **BDPG-1**? <br>
**A:** We were looking for a good name, and we were called internally `Big Data Project Group 1`. Lennert came up with
the idea to call the project **BDPG-1** and it had a good ring to it.
