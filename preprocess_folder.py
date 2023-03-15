import os
import shutil
from multiprocessing import Pool

# define paths
main_data_directory = '/media/akash/D591-2BFD/Datasets/Yoga-82/yoga_dataset_links'
store_data_directory = '/media/akash/D591-2BFD/Datasets/Yoga-82/Yoga-82'
train_directory = os.path.join(store_data_directory, 'train')
valid_directory = os.path.join(store_data_directory, 'valid')
test_directory = os.path.join(store_data_directory, 'test')

# create new directories
for directory in [train_directory, valid_directory, test_directory]:
    os.makedirs(directory, exist_ok=True)

# function to process each class folder
def process_folder(class_folder):
        # create train, valid, and test subfolders
    train_class_folder = os.path.join(train_directory, class_folder)
    valid_class_folder = os.path.join(valid_directory, class_folder)
    test_class_folder = os.path.join(test_directory, class_folder)
    os.makedirs(train_class_folder, exist_ok=True)
    os.makedirs(valid_class_folder, exist_ok=True)
    os.makedirs(test_class_folder, exist_ok=True)
        
        # loop through images
    image_list = os.listdir(os.path.join(main_data_directory, class_folder))
    for i, image_file in enumerate(image_list):
            # rename image file
        if i < int(len(image_list)*0.7):
            new_file_name = class_folder+'_image_'+str(i+1)+'.jpg'
            shutil.copy(os.path.join(main_data_directory, class_folder, image_file), os.path.join(train_class_folder, new_file_name))
        elif i < int(len(image_list)*0.9):
            new_file_name = class_folder+'_image_'+str(i+1)+'.jpg'
            shutil.copy(os.path.join(main_data_directory, class_folder, image_file), os.path.join(valid_class_folder, new_file_name))
        else:
            new_file_name = class_folder+'_image_'+str(i+1)+'.jpg'
            shutil.copy(os.path.join(main_data_directory, class_folder, image_file), os.path.join(test_class_folder, new_file_name))

# process each class folder in parallel
if __name__ == '__main__':
    class_folders = [f for f in os.listdir(main_data_directory) if os.path.isdir(os.path.join(main_data_directory, f))]
    with Pool() as p:
        p.map(process_folder, class_folders)

