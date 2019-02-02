# location-history

This is a python script attempting to create a heatmap of my Google location history. It makes use of the json and folium python libraries. json to import my location data from the json file Google provides, and folium to plot the points on a map.

I was able to optimize the program well enough to work with my ~800,000 data points, and it you want to give it a try, you can download your Google location history at [Google Takeout](https://takeout.google.com/settings/takeout). Place "Location History.json" in the same directory as the script, and it will output an HTML file displaying the map.

Here is an example of how it looks:

![locationdemo](https://user-images.githubusercontent.com/33944844/52169423-1d842f80-2706-11e9-8ee6-e11b2a94087b.png)
