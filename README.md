hacaton_project
==============================

I made a project through computer vision to help blind people on the street.

Project Organization
------------

    ├── LICENSE             <- MIT license file
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for individuals using this project
    ├── data
    │   ├── intermediate    <- Intermediate data that has been transformed
    │   ├── processed       <- The final, canonical data sets for modeling
    │   └── raw             <- The original, immutable data dump
    │
    │
    ├── models              <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                          the creator's initials, and a short `-` delimited description, e.g.
    │                          `1.0-ilm-initial-data-exploration`.
    │
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials
    │
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting
    |
    ├── results             <- Generated results from data analysis and fitting models
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                          generated with `pip freeze > requirements.txt`


--------
In this project I used Yolo model to segment street objects such as people, cars, traffic lights, road for people, road for cars and pedestrians.

Below I've outlined a complete guide for realizing this project.

![guise](references\\guide_for_project.jpg)

**Here is the training result for object segmentation**

![qadam](reports\figures\result_qadam_train\results.png) 

And the image test

![qadam](reports\output.png) 

**I also used the depth_pro tool to find the depth of the objects in the image. You can see the details here: https://github.com/apple/ml-depth-pro**

<p align="center">
  <img src="reports\object_detection_with_depth.jpg" alt="Image 1" width="400"/>
  <img src="reports\inverted_depth_map.jpg" alt="Image 2" width="400"/>
</p>

If you want to test just include app.py in the scripts folder

![qadam](scripts\processed\processed_photo_27_2024-10-23_01-45-34.jpg) 

Half of the project is written here. I'm sorry but I can't upload the full project.