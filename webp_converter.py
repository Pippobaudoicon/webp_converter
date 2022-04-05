from PIL import Image
import os

def convert_image_folder(image_path, image_type):

    im = Image.open(image_path)
    im = im.convert('RGB')
    image_name = image_path.split('/')[2].split('.')[0]
    print(f"Converting --> {image_name}")

    if image_type == 'jpg' or image_type == 'png':
        im.save(path+"/"+""f"{image_name}_converted.webp", 'webp')

def convert_image(image_path, image_type):

    im = Image.open(image_path)
    im = im.convert('RGB')
    image_name = image_path.split('.')[0]
    print(f"Converting --> {image_name}")

    if image_type == 'jpg' or image_type == 'png':
        im.save(f"{image_name}_converted.webp", 'webp')
    
choice = input("Cartella ('folder') o File singolo ('file')? ").lower()
if (choice == "folder"):
    path = "./"+input("Nome del path dentro questa cartella: ")
    files = os.listdir(path)
    print(files)
    images = [file for file in files if file.endswith(('jpg', 'png'))]


    for image in images:
        if image.endswith('jpg'):
            convert_image_folder(path+"/"+image, image_type='jpg')
        elif image.endswith('png'):
            convert_image_folder(path+"/"+image, image_type='png')
        else:
            print("Errore")
elif(choice == "file"):
    file_name = input("Nome del file (con tanto di estensione): ")
    if file_name.endswith('jpg'):
        convert_image(file_name, image_type='jpg')
    elif file_name.endswith('png'):
        convert_image(file_name, image_type='png')