import numpy as np
import pandas as pd
import torch
import warnings; warnings.filterwarnings('ignore')
from classes.NumberDataset import NumberDataset
from utils.performance_measure import precision_recall_f1
from models.EvenNet import EvenNet
import time
import argparse
import pickle

def train(batch_size_train, lr, epochs, is_verbose, weight_decay):
    """
    HYPERPARAMETERS AND CONSTANTS
        - BATCH_SIZE_TRAIN: size of the batches for training phase
        - LR: learning rate
        - N_EPOCHS: number of epochs to execute
        - IS_VERBOSE: to avoid too much output
        - WEIGHT_DECAY: the weight decay for the regularization in Adam optimizer
    """
    BATCH_SIZE_TRAIN = batch_size_train
    LR = lr
    N_EPOCHS = epochs
    IS_VERBOSE = is_verbose
    WEIGHT_DECAY = weight_decay
    """
    SETUP
    """
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    """
    DATA LOADING
        - Load all data: train, test, validation
    """

    model = EvenNet(input_dim=batch_size_train)
    """
    MODEL INITIALIZATION
        - optimizer: Adam with weight decay as regularization technique
        - loss function: binary cross entropy loss
    """
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    loss_function = torch.nn.MSELoss()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-ts', '--batchsizetrain', nargs=1, type=int, help='Size of the training batch', required=False)
    parser.add_argument('-lr', '--learningrate', nargs=1, type=float, help='Learning rate', required=False)
    parser.add_argument('-e', '--epochs', nargs=1, type=int, help='Number of epochs', required=False)
    parser.add_argument('-v', '--verbose', nargs=1, type=bool, help='Verbose mode on/off', required=False)
    parser.add_argument('-wd', '--weightdecay', nargs=1, type=float, help='Weight decay (L2 regularization)', required=False)
    args = parser.parse_args()
    train(
        batch_size_train=args.batchsizetrain[0] if args.batchsizetrain else 1000,
        lr=args.learningrate[0] if args.learningrate else 0.5,
        epochs=args.epochs[0] if args.epochs else 10,
        is_verbose=args.verbose if args.verbose else True,
        weight_decay=args.weightdecay[0] if args.weightdecay else 0.9
        )