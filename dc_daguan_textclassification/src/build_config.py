import argparse
import os


class ProjectConfig(object):
    def __init__(self):
        self.PROJECT_DIR = '/home/bp/PycharmProjects/dc_daguan_textclassification/dc_daguan_textclassification'
        self.SRC_DIR = os.path.join(self.PROJECT_DIR, 'src')
        self.DATA_DIR = os.path.join(self.PROJECT_DIR, 'data')
        self.args = None
        self.build_config()

    def build_config(self):
        arg_parser = argparse.ArgumentParser(description='Build configuration for Project.')
        arg_parser.add_argument('--train_data_path', type=str, default=os.path.join(self.DATA_DIR, 'train_set.csv'),
                                help='path of train dataset')
        arg_parser.add_argument('--test_data_path', type=str, default=os.path.join(self.DATA_DIR, 'test_set.csv'),
                                help='path of test dataset')
        self.args = arg_parser.parse_args()

if __name__ == '__main__':
    cfg = ProjectConfig()
    cfg.print_temp()
    # print(cfg.PROJECT_DIR)

    # print(cfg.args.train_data_path)
