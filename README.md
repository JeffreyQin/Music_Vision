# Music Vision

A Convolutional Neural Network trained 100% on original data to locate and identify note sequences from sheet music images into a computer readable format.

**Model Pipeline:**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

**Labelling Software:**

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)


## Using the Labelling Software

1. Store your raw data (sheet music images) in 'music_score/raw_images/', renaming image files is not needed.
2. Run ```cd label_software/```, then ```npm install```, then ```node app.js``` in the terminal to start backend services.
3. Open index.html with "live server" or equivalent, to see the following UI

<img width="403" alt="Screenshot 2024-02-13 115813" src="https://github.com/JeffreyQin/Music_Vision/assets/122770444/7a62838c-e6d7-49d4-a98f-533de77cab97">

Our label contains information about the durations and pitches of all notes in each chord present in the sheet music, as well as a vertical boundary coordinate for each chord. You can label the former by filling in the input fields, and the latter by clicking on the image to create the vertical boundary (as shown).

## Running the model

1. Run ```pip install -r requirements.txt```
2. Run ```python train_model.py``` to train a new model.
3. To evalute trained models, run ```python train_model.py --evaluate_saved``` instead.
