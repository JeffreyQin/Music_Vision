# Music Vision

A Convolutional Neural Network trained 100% on original data to locate and identify note sequences from sheet music images into a computer readable format.

Model Pipeline: Python (PyTorch, Scikit-learn, OpenCV, Matplotlib)

Labelling Software: JavaScript (express.js), HTML


## Using the Labelling Software

1. Store your raw data (sheet music images) in 'music_score/raw_images/', renaming image files is not needed.
2. Run ```cd label_software/```, then ```npm install```, then ```node app.js``` in the terminal to start backend services.
3. Open index.html with "live server" or equivalent, to see the following UI

<img width="403" alt="Screenshot 2024-02-13 115813" src="https://github.com/JeffreyQin/Music_Vision/assets/122770444/7a62838c-e6d7-49d4-a98f-533de77cab97">

Our label contains information about the durations and pitches of all notes in each chord present in the sheet music, as well as a vertical boundary coordinate for each chord. You can label the former by filling in the input fields, and the latter by clicking on the image to create the vertical boundary.

## Running the model

1. Run ```pip install -r requirements.txt```
2. Run ```python train_model.py``` to train a new model.
3. To evalute trained models, run ```python train_model.py --evaluate_saved``` instead.
