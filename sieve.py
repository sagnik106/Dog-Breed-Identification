import pandas as pd
import os

d=list(pd.read_csv("dog-breed-identification/labels.csv").values)
for img, fil in d:
    if not os.path.exists("dog-breed-identification/train/%s"%(fil)):
        os.makedirs("dog-breed-identification/train/%s"%(fil))
    os.rename("dog-breed-identification/train/%s.jpg"%(img), "dog-breed-identification/train/%s/%s.jpg"%(fil,img))