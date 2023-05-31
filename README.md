# chart_viewer
# Flask Image Gallery

This is a simple Flask application that displays a gallery of images from specified folders. You can switch between folders using buttons and view the images within each folder.

## Prerequisites

- Python 3.x
- Flask (install using `pip install flask`)

## Getting Started

1.Clone the repository:

   ```bash
   git clone <repository-url>

2. Install the required dependencies:
 pip install flask

3.Copy the folder containing your images into the application folder named "charts". Ensure that the structure is as follows:
    chart_viewer/charts 

4.Start the Flask development server by running the following command:
	python app.py

5. Open a web browser and go to http://localhost:5000 to access the application.

Modifying the resolution of images (300px --> 450px):
/templates/index.html 
	15.   grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); --> grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));

https://www.youtube.com/watch?v=uxZuFm5tmhM
