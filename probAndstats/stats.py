import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
        North,6.47,4.03
        Yorkshire,6.13,3.76
        Northeast,6.19,3.77
        East Midlands,4.89,3.34
        West Midlands,5.63,3.47
        East Anglia,4.52,2.92
        Southeast,5.89,3.20
        Southwest,4.79,2.71
        Wales,5.27,3.53
        Scotland,6.08,4.51
        Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alcoholMean = df['Alcohol'].mean()
alcoholMedian = df['Alcohol'].median()
alcoholMode = stats.mode(df['Alcohol'])
alcoholRange = max(df['Alcohol']) - min(df['Alcohol'])
alcoholStd = df['Alcohol'].std()
alcoholVariance = df['Alcohol'].var()

tobaccoMean = df['Tobacco'].mean()
tobaccoMedian = df['Tobacco'].median()
tobaccoMode = stats.mode(df['Tobacco'])
tobaccoRange  = max(df['Tobacco']) - min(df['Tobacco'])
tobaccoStd = df['Tobacco'].std()
tobaccoVariance = df['Tobacco'].var()

dictsToPrint = {
    'tobacco_dict' : {'mean' : ['tobacco', tobaccoMean ],
                'median' : ['tobacco',tobaccoMedian ],
                'mode' : ['tobacco',tobaccoMode ],
                'range' : ['tobacco',tobaccoRange ],
                'variance' : ['tobacco',tobaccoVariance ],
                'standard deviaton' : ['tobacco',tobaccoStd]
                    },
    'alcohol_dict' : {
                'mean' : ['Alcohol', alcoholMean],
                'median' : ['Alcohol', alcoholMedian],
                'mode' : ['Alcohol', alcoholMode],
                'range' : ['Alcohol', alcoholRange],
                'variance' : ['Alcohol', alcoholVariance],
                'standard deviaton' : ['Alcohol', alcoholStd]
                    }
                }

for dict in dictsToPrint:
    for list in dictsToPrint[dict]:
        print "The {0} for {1} in the Alcohol and Tobacco dataset is {2}".format(list, dictsToPrint[dict][list][0],dictsToPrint[dict][list][1])
