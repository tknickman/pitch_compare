## The Demo
Live [demo](http://orioles.thomasknickman.info/dashboard)

## The Data
The [dashboard](http://orioles.thomasknickman.info/dashboard) shows pitch metrics from all [pitchers](http://orioles.thomasknickman.info/pitchers)
included in the dataset that are filterable by:
* Day of Week
* Pitcher
* Opponent
* Specific Game
* Pitch Type
* Pitch Result
* Pitch Call
* Plate Appearance Result
* Pitch Speed
* Ball Count
* Strike Count
* Out Count

The five select lists at the top of the page, as well as each chart support multi selection, and display data in the form: `key: [pitch_count]`.
For example, the first select (Select Players) shows the number of pitches thrown by each pitcher with the current
set of filters. All filters are linked, and allow unlimited cross filtering.

For example, to see how many home runs were given up by Chris Tillman, against all games when playing the Boston Red Sox,
in the fourth or sixth inning, when the thrown pitch was a splitter - set the following filters:

1. Click "Chris Tillman" in the "Select Players" panel
2. Click "Boston Red Sox" bar in the "Pitches Per Opponent" panel
3. Click the "four", and "six" bar in the "Pitches Per Inning" panel
4. Click the "Splitter" item (either in the legend, or the pie chart segment) in the "Type of Pitch" panel

Then, by looking at the "Result of Plate Appearance" panel, it can be seen that with the current set
of filters, two home runs were given up.

This can be repeated indefinitely to create almost unlimited combinations of data. To remove the filter from
one panel, press the "Reset Selection" link at the bottom of each panel. To remove all filters, simply reload
the page.

## The Details

Front End:
1. [bootstrap](http://getbootstrap.com/2.3.2/)
2. [d3.js](https://d3js.org/)
3. [dc.js](https://dc-js.github.io/dc.js/)

Back End:
1. [pyramid](https://trypyramid.com/)
2. [python](https://www.python.org/)
