import argparse
import os


class ProjectConfig(object):
    def __int__(self,temp):
        self.project_dir = '/home/bp/PycharmProjects/dc_daguan_textclassification/dc_daguan_textclassification'
        self.src_dir = os.path.join(self.project_dir, 'src')
        self.DATA_DIR = os.path.join(self.project_dir, 'data')
        self.args = None
        self.build_config()
        self.temp = temp

    def build_config(self):
        arg_parser = argparse.ArgumentParser(description='Build configuration for Project.')
        arg_parser.add_argument('--train_data_path', type=str, default=os.path.join(self.DATA_DIR, 'train_set.csv'),
                                help='path of train dataset')
        arg_parser.add_argument('--test_data_path', type=str, default=os.path.join(self.DATA_DIR, 'test_set.csv'),
                                help='path of test dataset')
        self.args = arg_parser.parse_args()


    def print_temp(self):
        print(self.project_dir)

cfg = ProjectConfig('temp')
cfg.print_temp()
# if __name__ == '__main__':
#     cfg = ProjectConfig()
#     cfg.print_temp()
    # print(cfg.PROJECT_DIR)

    # print(cfg.args.train_data_path)
