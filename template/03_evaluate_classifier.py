import pandas as pd
import pickle  # for loading your trained classifier
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from template.extract_features import *  # our feature extraction


# The function that should classify new images.
# The image and mask are the same size, and are already loaded using plt.imread
def classify(img, mask):

    # Resize the image etc, if you did that during training

    model = pickle.load(open("logistic_regression_classifier.sav", "rb"))
    # Extract features (the same ones that you used for training)
    x = extract_features(img, mask)
    # Define column names
    columns = ['asymmetry', 'compactness','blue_white_veil','sd_r', 'sd_g', 'sd_b', 'mean_r', 'mean_g', 'mean_b', 
            'peak_r', 'peak_g', 'peak_b', ]
    single_row_df=   pd.DataFrame([x], columns=columns)
    prediction = model.predict(single_row_df)
    # print(x)
    # x = x.reshape(1, -1)

    # # Load the trained classifier

    # # Use it on this example to predict the label AND posterior probability
    pred_label = model.predict(single_row_df)
    print(prediction)
    pred_prob = model.predict_proba(single_row_df)

    # # print('predicted label is ', pred_label)
    # # print('predicted probability is ', pred_prob)
    return pred_label, pred_prob


images = os.listdir("data/test/images")

for image in images:
    img_path = f"data/test/images/{image}"
    mask = f"{image.split(".")[0]}_mask"
    mask_path = f"data/test/masks/{mask}.png"

    print(f"{image}::::{classify(img_path, mask_path)}")

# The TAs will call the function above in a loop, for external test images/masks
