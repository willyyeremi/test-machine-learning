# library

# data analytic library
import pandas
import numpy

# visualization library
import matplotlib.pyplot

# machine learning
import sklearn.model_selection
import missing_value
import categorical_handle
import ml_model

# loading data
data=pandas.read_csv(r"C:\Users\willy\Documents\Database\Kaggle\Melbourne Housing Snapshot\melb_data.csv")

# # list of numerical feature
# numerical_feature=['Rooms','Bedroom2','Bathroom','Car','Landsize','YearBuilt']

# # list of categorical column with each encoding representative
# list_column_OE=[]
# list_column_OHE=['Type','Method','Regionname']
# list_column_TE=['Suburb','SellerG','CouncilArea']

# # list of encoding
# categorical_data=[numerical_feature,list_column_OE,list_column_OHE]

# #choosing feature and target
# feature_list=[] # x is list of numerical columns that will be used as prediction material
# for x in categorical_data:
#     if len(x)!=0:
#         for y in x:
#             feature_list.append(y)

feature_list=['Rooms','Bedroom2','Bathroom','Car','Landsize']
feature=data[feature_list]
target=data.Price

# train test split method
a_data,b_data,a_target,b_target=sklearn.model_selection.train_test_split(feature,target,random_state=1)

# model
missing_value.missing_value(a_data,b_data,feature_list)
print(ml_model.multi_decision_tree(a_data,b_data,a_target,b_target,2,1000))