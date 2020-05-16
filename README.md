# Dog Breed Identification
### (Work in progress)
Wondering which breed the good boy was who you just crossed? Not to worry, because here is a computer vision project which does it for you.

## Dataset
The dataset is an imagenet subclass taken from [Kaggle](https://www.kaggle.com/c/dog-breed-identification/).

## Dataset Analysis
![Content](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/data_analysis.png)

# Model used
Resnet 152 v2- Pretrained on imagenet.<br/>
(taken from tf.keras.applications.resnet_v2)

# Model Performance
![Accuracy](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/data_analysis.png)<br/>
![Loss](https://github.com/sagnik106/Dog-Breed-Identification/blob/master/resources/data_analysis.png)

## Requirements
* Pandas 1.0.2
* Numpy 1.18.3
* Matplotlib 3.2.1
* Scikit-learn 0.22.2
* Tensorflow 2.2
* Tensor-dash 1.8.1