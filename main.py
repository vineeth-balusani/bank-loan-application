# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pickle
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


def print_metrics(y_test,y_pred):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted Labels")
    plt.ylabel("Actual Labels")
    f1_value = round(f1_score(y_test,y_pred,average='weighted',labels=np.unique(y_pred)),2)
    prec = round(precision_score(y_test,y_pred,average='weighted',labels=np.unique(y_pred)),2)
    rec = round(recall_score(y_test,y_pred,average='weighted',labels=np.unique(y_pred)),2)
    print("F1-score obtained is ",f1_value)
    print("Precision obtained is ",prec)
    print("Recall obtained is ",rec)
    return [f1_value,prec,rec]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "application_model.sav"
    loaded_model = pickle.load(open(filename, 'rb'))
    print(loaded_model)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
