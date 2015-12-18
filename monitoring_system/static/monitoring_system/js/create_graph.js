// this function filters the graph when the submit button is clicked
function filterChart(url) {

    var dataPoints = [];
    var org_name = document.getElementById("org_name").value;
    var type = document.getElementById("metric_type").value;
    var period = document.getElementById("time_period").value;
    var x = document.getElementById("datepicker_start").value;
    var y = document.getElementById("datepicker_end").value;


    $.ajax({
        type: "GET",
        url: url,
        data: {
            'org_name': org_name,
            'metric_type': type,
            'time_period': period,
            'start': x,
            'end': y
        },
        dataType: 'json',
        success: function(data) {
            console.log(data);

            if (data == "") {
                alert("No Data Found! Incorrect Organisation Name Entered.");
            }

            $.each(data, function(index, element) {
                xval = element.datetime
                yval = element.value
                var reggie = /(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})/
                var dateArray = reggie.exec(xval)
                var dateObject = new Date(
                    (+dateArray[1]),
                    (+dateArray[2]) - 1, // Careful, month starts at 0!
                    (+dateArray[3]),
                    (+dateArray[4]),
                    (+dateArray[5]),
                    (+dateArray[6])
                );


                var x = [new Date(dateObject), yval]
                dataPoints.push(x);

            });
            if (type == "CPU" || type == "") {

                g = new Dygraph(

                    // containing div
                    document.getElementById("line_chart"), dataPoints, {
                        drawPoints: true,
                        //showRoller: true,
                        labels: ['Date Time', 'Total'],
                        ylabel: 'Average Core Used (GB)',
                        strokeWidth: 1.5

                    }

                );
            }
            else if (type == "RAM") {
                g = new Dygraph(

                    // containing div
                    document.getElementById("line_chart"), dataPoints, {
                        drawPoints: true,
                        labels: ['Date Time', 'Total'],
                        ylabel: 'Average Ram Used (MB)',
                        strokeWidth: 1.5

                    }

                );
            }

        }
    }).fail(function() {
        alert('ERROR! \nAre the dates entered in the correct format ("YYYY-mm-dd")?');

    });


}
