# 6-04-21
## Group
- Discussed Project content
- Search for additional datasets on https://data.boston.gov/ 

## Bo
- Found out that in `test.csv` the following values have wrong values:
  - Lot Frontage
  - GarageYrBlt
  - MSZoning
  - MasVnrArea
  - Electrical
  - BldgType
- All numerical values are float, while all need to be changed to int, **except**:
  - `YearBuilt` needs to be Date
  - `YearRemodAdd` needs to be Date
  - `GarageYrBlt` needs to be Date
- Made Python function to detect inconsistencies
- Cleaned LotFrontage by replacing NaN values with Avg of all LotFrontages
- Cleaned illegal values in MSZoning

# 13-04-21
## Bo
- Transformed the following properties
  - `CentralAir`
  - All columns with a fix set of values
  - All Square feet to float
  - All year to Date Datatype
  - Merged `YrSold` & `MoSold` to `SoldDate`
  
# 14-04-21
## Bo
- Fully cleaned test.csv and train.csv
- Fixed relationships between certain values *(E.G. When GarageType is `NA`, the build Year was filled in.)*