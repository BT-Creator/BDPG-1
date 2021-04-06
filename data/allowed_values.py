# This file contains all parameters that are allowed in the dataset.
# With this, you can quickly check if there is false data in the columns (If the parameters are defined)
# The variable names matches the column name in test.csv and train.csv
MSSubClass = [20, 30, 40, 45, 50, 60, 70,
              75, 80, 85, 90, 120, 150, 160, 180, 190]
MSZoning = ["A", "C", "FV", "I", "RH", "RL", "RP", "RM"]
Street = ["Grvl", "Pave"]
Alley = ["Grvl", "Pave", None]
LotShape = ["Reg", "IR1", "IR2", "IR3"]
LandContour = ["Lvl", "Bnk", "HLS", "Low"]
Utilities = ["AllPub", "NoSewr", "NoSeWa", "ELO"]
LotConfig = ["Inside", "Corner", "CulDSac", "FR2", "FR3"]
LandSlope = ["Gtl", "Mod", "Sev"]
Neighborhood = ["Blmngtn", "Blueste","BrDale", "BrkSide", "ClearCr", "CollgCr", "Crawfor",
                "Edwards", "Gilbert", "IDOTRR", "MeadowV", "Mitchel", "Names", "NoRidge",
                "NPkVill", "NridgHt", "NWAmes","OldTown", "SWISU", "Sawyer", "SawyerW", "Somerst",
                "StoneBr", "Timber", "Veenker"]
Condition1 = ["Artery", "Feedr", "Norm", "RRNn", "RRAn", "PosN", "PosA", "RRNe", "RRAe"]
Condition2 = ["Artery", "Feedr", "Norm", "RRNn","RRAn", "PosN", "PosA", "RRNe", "RRAe", None]
BldgType = ["1Fam", "2FmCon", "Duplx", "TwnhsE", "TwnhsI"]
HouseStyle = ["1Story", "1.5Fin", "1.5Unf", "2Story", "2.5Fin", "2.5Unf", "SFoyer", "SLvl"]
OverallQual = range(1,10)
OverallCond = range(1,10)
RoofStyle = ["Flat", "Gable", "Gambrel", "Hip", "Mansard", "Shed"]
RoofMatl = ["ClyTile", "CompShg", "Membran", "Metal", "Roll", "Tar&Grv", "WdShake", "WdShngl"]
Exterior1st = ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard",
               "ImStucc", "MetalSd", "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd"
               "Wd Sdng", "WdShing"]
Exterior2nd = ["AsbShng", "AsphShn", "BrkComm", "BrkFace", "CBlock", "CemntBd", "HdBoard",
               "ImStucc", "MetalSd", "Other", "Plywood", "PreCast", "Stone", "Stucco", "VinylSd"
               "Wd Sdng", "WdShing", None]
MasVnrType = ["BrkCmn", "BrkFace", "CBlock", None, "Stone"]
