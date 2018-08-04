import pandas as pd

from build_config import ProjectConfig

cfg = ProjectConfig()
print(cfg.PROJECT_DIR)
print(cfg.PROJECT_DIR)
train_data_csv = pd.read_csv(cfg.args.train_data_path)
test_data_csv = pd.read_csv(cfg.args.test_data_path)

print('train_data_csv.shape : {}'.format(train_data_csv.shape))
print('test_data_csv.shape : {}'.format(test_data_csv.shape))

print('train_data_csv.columns : {}'.format(train_data_csv.columns))
print('test_data_csv.columns : {}'.format(test_data_csv.columns))


