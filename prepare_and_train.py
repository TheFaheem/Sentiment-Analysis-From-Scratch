# Importing All the Modules that we created
from data_initializer import DataInitializer
from dataset_preparer import DatasetPreparer
from dataset_preprocessor import DataPreprocessor
from batch_iterator import BatchIterator
from trainer import Trainer


class Prepare_Train():

    def __init__(self, dataset_dir, train_json_path, test_json_path, batch_size):

        self.dataset_dir = dataset_dir
        self.train_json_path = train_json_path
        self.test_json_path = test_json_path
        self.batch_size = batch_size

    def initialize_the_dataset(self):
    
        # Initialize the Dataset Directory
        initialize_dataset = DataInitializer(self.dataset_dir)
        self.dataset_folder = initialize_dataset.prepare_dataset_folder()

    def prepare_the_dataset(self):
    
        dataset_prep = DatasetPreparer(self.dataset_folder)
        self.train_x, self.train_y, self.test_x, self.test_y = dataset_preparer.prepare_dataset(self.train_json_path, self.test_json_path, verbose=True)
        self.vocab_path =  dataset_prep.build_vocab()

    def preprocess_the_dataset(self):
        
        preprocess_dataset = DataPreprocessor(self.vocab_path)
        self.vocab = preprocess_dataset.load_vocab(self.vocab_path)
        preprocess_dataset.check(self.train_x, self.train_y, self.test_x, self.test_y, before=True)
        self.filtered_train_x, self.filtered_train_y, self.filtered_test_x, self.filtered_test_y = preprocess_dataset.filter_by_length(self.train_x, self.train_y, self.test_x, self.test_y)
        preprocess_dataset.check(self.filtered_train_x, self.filtered_train_y, self.filtered_test_x, self.filtered_test_y, before=False)
        self.tokenize = preprocess_dataset.tokenize

    def initialize_the_iterator(self):

        iterator = BatchIterator(self.filtered_train_x, self.filtered_train_y, self.filtered_test_x, self.filtered_test_y, self.tokenize)
        self.train_generator = iterator.data_generator(self.batch_size, train=True)
        self.test_generator = iterator.data_generator(self.batch_size, train=False)
        self.batch_per_epoch_train, self.batch_per_epoch_test = iterator.calculate_batch_per_epoch(self.batch_size)
        
