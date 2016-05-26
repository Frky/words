var last_wid;
var wstart, wstop;
var range;

var refresh_data = function() {
    last_wid = parseInt($("#last_wid").val());
    wstart = parseInt($("#wstart").val());
    wstop = parseInt($("#wstop").val());
    return;
}

var refresh_words = function() {
    $.ajax({
                url: "ajax_words",
            }).done(function(data) {
        $("#words-content").html(data);
        refresh_data();
    });
}

var update_timeline = function(start, stop) {
    $(".word").each(function() {
        var wid = parseInt($(this).attr("data-wid"));
        if (wid < start || wid > stop)
            $(this).fadeOut();
        else
            $(this).fadeIn();
    });

}

$(document).ready(function() {
    range = $("#timeline")[0];
    console.log(range);

    refresh_data();

    noUiSlider.create(range, {
        start: [ wstart , wstop ], // Handle start position
        step: 1, // Slider moves in increments of '10'
        margin: 0, // Handles must be more than '20' apart
        connect: true, // Display a colored bar between the handles
        direction: 'ltr', // Put '0' at the bottom of the slider
        behaviour: 'tap-drag', // Move handle on tap, bar is draggable
        range: { // Slider can select '0' to '100'
            'min': 1,
            'max': wstop
        },
        pips: { // Show a scale with the slider
            mode: 'positions',
            values: [0, 100],
            stepped: false,
            density: 100,
        }
    });

    range.noUiSlider.on('change', function() {
        update_timeline(range.noUiSlider.get()[0], range.noUiSlider.get()[1]);
    });

    setInterval(function() {
        jQuery.ajax({
                        url: "get_last_word",
                    }).done(function(data) {
                        if (data > last_wid) {
                            last_wid = data;
                            refresh_words();
                        }
                });
    }, 2000);
   
    $("#id_word").focus();
});
