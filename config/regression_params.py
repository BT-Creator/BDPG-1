"""Contains variables used to configure the regression behavior
- `reg_params` values are parameters used to prepare the data for regression
"""

reg_params = {
    'target_column': 'SalePrice',
    'test_size': 0.3,
    'random_state': 33,
    'cv': 5
}