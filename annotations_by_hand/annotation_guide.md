Annotation guide

We are given annotation by-hand of our set of images as a task for our project. For this we need to establish an annotation guide describing how to precisely rate the visual features of skin lesions on the images.	

For this task we had to look up a few related annotation works done by dermatologists online and think of an approach based on these. Afterwards, we discussed 5 images together and agreed on how to rate following features: Asymmetry of skin lesion, Compactness of skin lesion, Blue-white veil presence on skin lesion. 

We have decided that we will not include Color of skin lesion in our by-hand annotation for the following reason. Color perception is highly subjective and it varied among us. We have found out that describing precise colors in skin lesions was challenging due to variations and multiple hues. Considering time constraints and prioritizing more relevant features, color annotation was excluded to focus on more easily annotated features.

For each of our three features we will be assigning a numerical value.

Asymmetry - Dermatologists rated the asymmetry of lesions on a scale from 0 to 1, where 0 indicated lesions with highly irregular borders and 1 indicated lesions with perfect symmetry. This approach has inspired us in making the rules for our annotation:

- Lesion Appears Not Symmetrical: Assign a value between 0 and 0.5. This acknowledges asymmetry and allows for a range to capture varying degrees of asymmetry within the lesion.
- Lesion Appears Symmetrical on at Least One Axis (X or Y): Assign a value between 0.5 and 0.75. This recognizes partial symmetry and provides a range to reflect asymmetry along one axis.
- Lesion Appears Symmetrical on Multiple Axes: Assign a value between 0.75 and 1. This indicates a highly symmetrical lesion, acknowledging symmetry along multiple axes.

Compactness – Similar reasoning to asymmetry:

- Lesion Appears Fragmented or Dispersed: Assign a value between 0 and 0.5. This indicates that the lesion's features are spread out or fragmented, suggesting low compactness.
- Lesion Appears Tightly Packed: Assign a value between 0.5 and 1. This indicates that the lesion's features are closely packed together, suggesting high compactness.

Blue-white veil - Binary annotation approach was used in some related work, assigning a value of 0 for lesions without a blue-white veil and 1 for lesions exhibiting this feature:

- Presence of Blue-White Veil: Assign a value of 1 if there is any discernible blue-white coloration within the lesion.
- Absence of Blue-White Veil: Assign a value of 0 if there is no discernible blue-white coloration within the lesion. 

All the by-hand annotations are documented in CSV file.
