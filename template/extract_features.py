import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# importing custom created functions
from features.asymmetry import *
from features.compactness import *
from features.blue_white_veil import *
from features.histogram_data import *


# Main function to extract features from an image, that calls other functions
def extract_features(image: str, mask: str):
    """returns [a, c, bwv, sd_{r,g,b}, m_{r,g,b}, p_{r,g,b}]"""
    a = get_asymmetry(mask_path=mask)
    c = get_compactness(mask)

    bwv = get_blue_white_veil(image_path=image, mask_path=mask)
    h = get_histogram_data(img_path=image, mask_path=mask)
    if h is None:
        raise Exception("histogram data is missing")
    sd_r = h["r"]["std_dev"]
    sd_g = h["g"]["std_dev"]
    sd_b = h["b"]["std_dev"]

    m_r = h["r"]["mean"]
    m_g = h["g"]["mean"]
    m_b = h["b"]["mean"]

    p_r = h["r"]["peak_val"]
    p_g = h["g"]["peak_val"]
    p_b = h["b"]["peak_val"]

    return np.array(
        [a, c, bwv, sd_r, sd_g, sd_b, m_r, m_g, m_b, p_r, p_g, p_b], dtype=np.float16
    )
