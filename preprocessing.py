import numpy as np
def preprocess_features(df):   # must accept y=None
    X = df.copy()

    # Outlier handling
    if 'Expected_Customers' in X.columns:
        Q1 = X["Expected_Customers"].quantile(0.25)
        Q3 = X["Expected_Customers"].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
    
        X["Expected_Customers"] = np.where(X["Expected_Customers"] < lower_bound, lower_bound,
                          np.where(X["Expected_Customers"] > upper_bound, upper_bound, X["Expected_Customers"]))
        

    # Feature engineering
    if {'Previous_Day_Consumption','Previous_Week_Same_Day'}.issubset(X.columns):
        X['Historical_Trend'] = (X['Previous_Day_Consumption'] + X['Previous_Week_Same_Day']) / 2

    if {'Expected_Customers','Previous_Day_Consumption'}.issubset(X.columns):
        X['Demand_Lag'] = X['Expected_Customers'] - X['Previous_Day_Consumption']

    # Feature selection
    selected_features = [
        'Expected_Customers',
        'Weather',
        'Festival',
        'Day_of_Week',
        'Historical_Trend',
        'Demand_Lag'
    ]
    return X[selected_features]