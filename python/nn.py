import sys
import os
repo_path = '../commbank_api'
sys.path.append(os.path.abspath(repo_path))
import qq


def retreive_data_from_api():
    return qq.retrive_data()