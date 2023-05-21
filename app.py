import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Define the path to the folder containing folders with images
image_folder_path = "./charts"

# Get the list of folder names
folder_names = [name for name in os.listdir(image_folder_path) if os.path.isdir(os.path.join(image_folder_path, name))]

@app.route('/')
def index():
    return render_template('index.html', folder_names=folder_names)

@app.route('/show_images/<folder_name>')
def show_images(folder_name):
    # Get the path to the selected folder
    folder_path = os.path.join(image_folder_path, folder_name)

    # Get the list of image file names in the folder
    image_file_names = [name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))]

    return render_template('index.html', folder_names=folder_names, selected_folder=folder_name, image_file_names=image_file_names)

@app.route('/images/<folder_name>/<image_file_name>')
def get_image(folder_name, image_file_name):
    return send_from_directory(os.path.join(image_folder_path, folder_name), image_file_name)

if __name__ == '__main__':
    app.run(debug=True)
