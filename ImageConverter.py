import sys
import os
from PIL import Image

# grab input and output folders from terminal
def get_directories():
    try:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        min_res = int(sys.argv[3])
        max_res = int(sys.argv[4])

    except IndexError as e:
        print(f'Add more arguments, {sys.argv[1:2]}: {e}')

    except (ValueError) as e:
        print(f'3rd and 4th arguments must be integers: {e}')

    else: 
        return input_folder, output_folder, min_res, max_res


# check if output folder exists, if not create it
def check_path_exists(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


def image_filtering(image, min_res = 500, max_res = 500):
    try:
        resized_img = image.resize((min_res, max_res))
        # turn to grey scale
        filtered_img = resized_img.convert('P') 

    except IndexError as e:
        print(f'Need 2 resolution values, defaulting to original sizes: {e}')
    
    else:
        return filtered_img


# convert images to png, crop and save
def convert_save_images(input_folder, output_folder, min_res, max_res):
    try:
        for i, infile in enumerate(os.listdir(input_folder)):
            image = Image.open(f'{input_folder}{infile}')
            
            # image converting
            filtered_img = image_filtering(image, min_res, max_res)

            outfile = os.path.splitext(infile)[0]
            filtered_img.save(f'{output_folder}{outfile}.png', 'png')
            print(f'Image {i+1} converted')

    except FileNotFoundError as e:
        print(f'Incorrect original image folder. Check path: {e}')

    except (AttributeError):
        print('Read above')


# main
if __name__ == '__main__':
    input_folder, output_folder, min_res, max_res = get_directories()
    check_path_exists(output_folder)
    convert_save_images(input_folder, output_folder, min_res, max_res)