window.onload = function () {

    var options = {
        title: {
            text: "Customers and number of new leads"
        },
        subtitles: [{
            text: "As of November, 2018"
        }],
        animationEnabled: true,
        data: [{
            type: "pie",
            startAngle: 40,
            toolTipContent: "<b>{label}</b>: {y}%",
            showInLegend: "true",
            legendText: "{label}",
            indexLabelFontSize: 16,
            indexLabel: "{label} - {y}%",
            dataPoints: [
                { y: 7, label: "Masaki Fujimoto" },
                { y: 3, label: "Joe Smith" },
                { y: 7, label: "Ryan Owen" },
                { y: 4, label: "Michael Choi" },
          
            ]
        }]
    };
    $("#chartContainer").CanvasJSChart(options);
    
    }