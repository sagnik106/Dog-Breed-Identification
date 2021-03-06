# Dog Breed Identification
### (Work in progress)
Wondering which breed the good boy was who you just crossed? Not to worry, because here is a computer vision project which does it for you.

## Dataset
The dataset is an imagenet subclass taken from [Kaggle](https://www.kaggle.com/c/dog-breed-identification/).

## Dataset Analysis
![Content](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/data_analysis.png)

## Model used
Resnet 152 v2- Pretrained on imagenet.<br/>
(taken from tf.keras.applications.resnet_v2)

## Model Performance
![Accuracy](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/accuracy.png)<br/>
![Loss](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/loss.png)

## Requirements
* Pandas 1.0.2
* Numpy 1.18.3
* Matplotlib 3.2.1
* Scikit-learn 0.22.2
* Tensorflow 2.2
* Tensor-dash 1.8.1

## File Configuration
* [trainer.ipynb](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/trainer.ipynb) - Jupyter notebook which has the analysis of dataset and the declaration and training of the model
* [sieve.py](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/sieve.py) - Organizes the dataset in the format accepted by the flow_from_directory method of Image DataGenerator method.
* [resources/](https://github.com/sagnik106/Dog-Breed-Identification/tree/master/resources) - Github README resources