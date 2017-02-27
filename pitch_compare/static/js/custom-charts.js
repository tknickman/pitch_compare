var pitchEventRingChart = dc.pieChart("#chart-ring-pitch-event"),
    pitchEventResultRingChart = dc.pieChart("#chart-ring-pitch-event-result"),
    pitchTypeRingChart = dc.pieChart("#chart-ring-pitch-type"),
    pitchCallRingChart = dc.pieChart("#chart-ring-pitch-call"),
    pitchesPerDay = dc.rowChart("#chart-row-pitch-day"),
    pitchPerOpponent = dc.barChart("#chart-row-pitch-per-opponent"),
    playerSelect = dc.selectMenu('#player-select'),
    pitchesPerInning = dc.barChart("#chart-bar-pitches-per-inning"),
    pitchSpeedPerInning = dc.seriesChart("#chart-bar-pitch-speed-per-inning"),
    gameSelect = dc.selectMenu('#game-select'),
    prevStrikeSelect = dc.selectMenu('#previous-strike-select'),
    prevBallSelect = dc.selectMenu('#previous-ball-select'),
    prevOutSelect = dc.selectMenu('#previous-out-select'),
    pitchLocationScatterPlot = dc.scatterPlot("#chart-scatter-pitch-location", 'pitchLocation'),
    pitchData = [];

// build the URL, and make a simple GET ajax request to the backend
$.get('/data/pitch', function(data) {
    // request was successful, but there were no results returned
    if (data.status === 'ok') {
        // show error to user indicating lack of results
        pitchData = data.pitch_data;
        build_chart()
    }
    else {
        // show error to user indicating failure
        alert('Error retrieving data, please contact tknickman@gmail.com');
    }

});



function build_chart() {

    // set crossfilter
    var ndx = crossfilter(pitchData),

        // game data
        gameName  = ndx.dimension(function(d) {return d.game_display_name; }),
        pitcherName = ndx.dimension(function(d) { return d.player_name; }),
        dayOfWeek  = ndx.dimension(function(d) {return d.game_day; }),
        opponentName  = ndx.dimension(function(d) {return d.opponent; }),
        inningNum  = ndx.dimension(function(d) {return d.inning; }),

        // pre data
        preStrikes = ndx.dimension(function(d) { return d.pre_strikes; }),
        preBalls = ndx.dimension(function(d) { return d.pre_balls; }),
        preOuts = ndx.dimension(function(d) { return d.pre_outs; }),

        // pitch data
        pitchEvent  = ndx.dimension(function(d) {return d.event_type; }),
        pitchEventResult  = ndx.dimension(function(d) {return d.event_result; }),
        pitchCall = ndx.dimension(function(d) {return d.ball_strike_other; }),
        pitchType  = ndx.dimension(function(d) {return d.pitch_type; }),
        pitchDimension  = ndx.dimension(function(d) {return [d.game_id, d.inning]; }),

        pitchLocation = ndx.dimension(function(d) {return [+d.plate_x, +d.plate_z]; }),
        pitchDimensionGroup = pitchDimension.group().reduce(
            function (p, v) {
                ++p.number;
                p.total += +v.initial_speed;
                p.avg = Math.round(p.total / p.number);
                return p;
            },
            function (p, v) {
                --p.number;
                p.total -= +v.initial_speed;
                p.avg = (p.number == 0) ? 0 : Math.round(p.total / p.number);
                return p;
            },
            function () {
                return {number: 0, total: 0, avg: 0}
            }
        );

    /////////////////
    // RING CHARTS //
    /////////////////


    // RESULT OF PLATE APPEARANCE
    pitchEventRingChart
        .height(500)
        .dimension(pitchEventResult)
        .group(pitchEventResult.group())
        .legend(dc.legend().legendText(function(d, i) {
            return d.name + ': ' + d.data;
        }))
        .innerRadius(35)
        .on('pretransition', function(chart) {
            chart.selectAll('text.pie-slice').text(function(d) {
                return '';
            })
        })
        .controlsUseVisibility(true);

    // RESULT OF PITCH
    pitchEventResultRingChart
        .height(400)
        .dimension(pitchEvent)
        .group(pitchEvent.group())
        .legend(dc.legend().legendText(function(d, i) {
            return d.name + ': ' + d.data;
        }))
        .innerRadius(35)
        .on('pretransition', function(chart) {
            chart.selectAll('text.pie-slice').text(function(d) {
                return '';
            })
        })
        .controlsUseVisibility(true);

    // PITCH TYPE
    pitchTypeRingChart
        .height(200)
        .dimension(pitchType)
        .group(pitchType.group())
        .legend(dc.legend().legendText(function(d, i) {
            return d.name + ': ' + d.data;
        }))
        .innerRadius(35)
        .on('pretransition', function(chart) {
            chart.selectAll('text.pie-slice').text(function(d) {
                return '';
            })
        })
        .controlsUseVisibility(true);

    // BALL | STRIKE | OTHER
    pitchCallRingChart
        .height(200)
        .dimension(pitchCall)
        .group(pitchCall.group())
        .legend(dc.legend().legendText(function(d, i) {
            return d.name + ': ' + d.data;
        }))
        .innerRadius(35)
        .on('pretransition', function(chart) {
            chart.selectAll('text.pie-slice').text(function(d) {
                return '';
            })
        })
        .controlsUseVisibility(true);



    ////////////////
    // BAR CHARTS //
    ////////////////


    pitchesPerInning
        .height(250)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel('Inning')
        .elasticX(true)
        .elasticY(true)
        .yAxisLabel('Number of Pitches Thrown')
        .dimension(inningNum)
        .barPadding(0.1)
        .outerPadding(0.05)
        .group(inningNum.group())
        .controlsUseVisibility(true);
    pitchesPerInning.margins().left += 15;

    pitchPerOpponent
        .height(400)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .brushOn(false)
        .xAxisLabel('Team')
        .elasticX(true)
        .elasticY(true)
        .yAxisLabel('Pitches Thrown')
        .dimension(opponentName)
        .barPadding(0.1)
        .outerPadding(0.05)
        .controlsUseVisibility(true)
        .group(opponentName.group());
    pitchPerOpponent.margins().left += 15;
    pitchPerOpponent.margins().bottom += 60;

    pitchesPerDay
        .height(250)
        .dimension(dayOfWeek)
        .group(dayOfWeek.group())
        .elasticX(true)
        .controlsUseVisibility(true)
        .xAxis().ticks(4);


    ///////////////////
    // SERIES CHARTS //
    ///////////////////


    pitchSpeedPerInning
        .height(400)
        .chart(function(c) { return dc.lineChart(c).interpolate('basis'); })
        .x(d3.scale.linear().domain([1,9]))
        .yAxisLabel("Average Pitch Speed")
        .xAxisLabel("Inning")
        .brushOn(false)
        .dimension(pitchDimension)
        .group(pitchDimensionGroup)
        .seriesAccessor(function(d) {return "Expt: " + d.key[0];})
        .keyAccessor(function(d) {return +d.key[1];})
        .valueAccessor(function(d) {return +d.value.avg;});
    pitchSpeedPerInning.yAxis().tickFormat(function(d) {return d3.format(',d')(d);});
    pitchSpeedPerInning.margins().left += 40;


    //////////////////
    // SELECT LISTS //
    //////////////////


    playerSelect
        .dimension(pitcherName)
        .multiple(true)
        .group(pitcherName.group())
        .controlsUseVisibility(true);

    gameSelect
        .dimension(gameName)
        .multiple(true)
        .group(gameName.group())
        .controlsUseVisibility(true);

    // prev event select
    prevStrikeSelect
        .dimension(preStrikes)
        .multiple(true)
        .group(preStrikes.group())
        .controlsUseVisibility(true);

    prevBallSelect
        .dimension(preBalls)
        .multiple(true)
        .group(preBalls.group())
        .controlsUseVisibility(true);

    prevOutSelect
        .dimension(preOuts)
        .multiple(true)
        .group(preOuts.group())
        .controlsUseVisibility(true);
    prevOutSelect.on('postRender', function () { $(".main-panel").LoadingOverlay("hide", true); });

    // RENDER ALL CHARTS
    dc.renderAll();

}

