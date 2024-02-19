import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import customexception
import os
import sys
from dataclasses import dataclass
from pathlib import Path


from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.utils.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformation(self):
        try:
            logging.info('Data Transformation initiated')
            
            cat_cols=['seller_type', 'layout_type', 'property_type', 'furnish_type']
            num_cols=...
            pass
        
        except:
            pass
        
    def initialize_data_transformation(self,train_path,test_path):
        ...                