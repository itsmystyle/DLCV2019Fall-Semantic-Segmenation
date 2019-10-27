from __future__ import absolute_import
import os

import argparse


def arg_parse():
    parser = argparse.ArgumentParser(
        description="DLCV HW2 in image segmentation using pytorch"
    )

    # Datasets parameters
    parser.add_argument(
        "--data_dir",
        type=str,
        default=os.path.join("hw2_data"),
        help="root path to data directory",
    )
    parser.add_argument(
        "--workers",
        default=4,
        type=int,
        help="number of data loading workers (default: 4)",
    )

    # Models parameters
    parser.add_argument("--save_dir", type=str, default="models")
    parser.add_argument("--pretrained", dest="pretrained", action="store_true")

    # Training parameters
    parser.add_argument(
        "--gpu", default=0, type=int, help="gpu device ids for CUDA_VISIBLE_DEVICES"
    )
    parser.add_argument(
        "--epoch", default=100, type=int, help="num of validation iterations"
    )
    parser.add_argument(
        "--val_epoch", default=1, type=int, help="num of validation iterations"
    )
    parser.add_argument("--train_batch", default=32, type=int, help="train batch size")
    parser.add_argument("--test_batch", default=32, type=int, help="test batch size")
    parser.add_argument(
        "--lr", default=0.0002, type=float, help="initial learning rate"
    )
    parser.add_argument(
        "--weight-decay", default=0.0005, type=float, help="initial learning rate"
    )

    # resume trained model
    parser.add_argument(
        "--resume", type=str, default="", help="path to the trained model"
    )

    # others
    parser.add_argument("--random_seed", type=int, default=42)

    args = parser.parse_args()

    return args