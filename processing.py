# processing.py
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def separar_variables(df, objetivo):
    X = df.drop(columns=[objetivo])
    y = df[objetivo]
    return X, y

def normalizar_minmax(X_train, X_test):
    scaler = MinMaxScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm  = scaler.transform(X_test)
    return X_train_norm, X_test_norm, scaler

def split_train_test(X, y, test_size=0.30, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
