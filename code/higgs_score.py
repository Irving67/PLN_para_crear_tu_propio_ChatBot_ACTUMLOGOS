import numpy as np
from sklearn.metrics import roc_auc_score


def AMSScore(s, b):
    return np.sqrt(2. * ((s + b + 10.) * np.log(1. + s / (b + 10.)) - s))


def evaluate(Y_true_train, Y_pred_train, w_train, Y_true_test, Y_pred_test, w_test):
    '''Evaluate a higg boson prediction.

    Args:
        Y_true_train
        Y_pred_train
        w_train
        Y_true_test
        Y_pred_test
        w_test
    Returns:
        score_train, score_test
    '''
    ratio = float(len(w_train)) / float(len(w_test))
    TruePositive_train = w_train * (Y_true_train == 1.0) * (1.0 / ratio)
    TrueNegative_train = w_train * (Y_true_train == 0.0) * (1.0 / ratio)
    TruePositive_valid = w_test * (Y_true_test == 1.0) * (1.0 / (1 - ratio))
    TrueNegative_valid = w_test * (Y_true_test == 0.0) * (1.0 / (1 - ratio))
    s_train = sum(TruePositive_train * (Y_pred_train == 1.0))
    b_train = sum(TrueNegative_train * (Y_pred_train == 1.0))
    s_test = sum(TruePositive_valid * (Y_pred_test == 1.0))
    b_test = sum(TrueNegative_valid * (Y_pred_test == 1.0))
    score_train = AMSScore(s_train, b_train)
    score_test = AMSScore(s_test, b_test)
    print('--- Resultados --')
    print(
        '- AUC train: {:.3f} '.format(roc_auc_score(Y_true_train, Y_pred_train)))
    print(
        '- AUC test : {:.3f} '.format(roc_auc_score(Y_true_test, Y_pred_test)))
    print('- AMS train: {:.3f} sigma'.format(score_train))
    print('- AMS test : {:.3f} sigma'.format(score_test))
    return score_train, score_test
