# Blog 3 - First Publication Reflection (10/19/2025)

You can read the paper and conference slides [here](https://shoesareme.github.io/projects/research/dcuhi).

## Theoretical Methods Discussion

Let $$T_{\textrm{Date}}(x,y) = \textrm{Temperature on date at x, y}$$. We want to know the change in $$T$$ as $$\textrm{Date}$$ changes. But this is pretty hard (and pretty informal). We want to know the average change over the whole region in a sense. Thus, let 

$$
\bar{T}(t) = \frac{\sum_{(x,y) \in \textrm{ROI}} T_{t}(x,y)}{\|\textrm{ROI}\|}.
$$

We want to find or approximate $$\frac{\mathrm{d}\bar{T}}{\mathrm{d}t}$$. Through hand-waving, we can say that

$$
\frac{\mathrm{d}\bar{T}}{\mathrm{d}t} \approx \frac{\partial T}{\partial t}.
$$

This is heavily informal mathematically-wise (also an abuse of notation), but the point is to convey the idea behind the study. We try to use a variety of different things to approximate this, including finite differences $$\Delta$$, calculating means/medians over different factors, and more. This requires a lot of data, which makes us downscale data based on NDVI and similar indicies. All of this was/can be implemented via a python script which can be found on the link above. Specifically, the python scripts allow for a lot of customization so some of the methods are available on the script directly but other methods may not be included on the script directly, but can be easily implemented. The explanation for all the methods are available in the readme for the script.

## Future Directions

There are quite a few interesting avenues for future research. Better ML models can fix some of the issues of the random forest predictions, as well as more metrics to approximate $$\frac{\mathrm{d}\bar{T}}{\mathrm{d}t}$$. Additionally, there should be research into how the CLHI or air termperature play a role. And obviously, there should be attempts to solve this problem.

Perhaps I will revisit this problem from a new angle in the future, I am already considering different approaches currently.

## Musings

Before starting the project, I had learned quite a bit about computer science (a field that I am interested in). So I wanted to apply this knowledge to a problem that is important. This project taught me a lot about the research and presentation process. I am grateful to Dr. Bo Zhao for guiding me through this project.
