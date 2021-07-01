# 20210701_Facebook_Poster
Auto poster using for https://www.facebook.com/progress20XX


## config.json
1. replace user access token
2. pie_colors = [sub_color, main_color]


## io.py: main program
- uses multiprocessing with 16 workers
- input format: yy%%% **(%%%=1000 not available)**


## upload_files.py
- gets page access token
- deletes the created images
- uses requests to post requests to facebook API


## pie.py
- uses matplotlib to plot
- image(*yy%%%.jpg*) size: 1000x1000 px diameter: 900 px
- uses datetime to get time

## Requirements
1. python 3.6+
2. matplotlib
3. datetime
4. requests

## References 
- [Facebook API Page Photos](https://developers.facebook.com/docs/graph-api/reference/page/photos/)
- [Facebook API access tokens](https://developers.facebook.com/docs/pages/access-tokens)
- [Upload by requests](https://www.reddit.com/r/learnpython/comments/5677wn/uploading_jpg_to_facebook_through_graph_api/)
- [matplotlib](https://matplotlib.org/)
