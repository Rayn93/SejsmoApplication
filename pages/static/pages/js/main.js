$(window).scroll(function() {
    if ($(this).scrollTop() > 1){
        $('#header-top').addClass("sticky");
    }
    else{
        $('#header-top').removeClass("sticky");
    }
});



$(document).ready(function () {

// OSKRYPTOWANIE DLA MENU

    var $height = $(window).height();

    $("#homepage header, header #myCarousel .item").css("height", $height);

    $("#header-top .traggle-menu").css("height", $height);

    $("#header-top .burger").click(function () {
        $(".traggle-menu").show("slide", { direction: "left" }, 500);
    });

    $(".close").click(function () {
        $(".traggle-menu").hide("slide", "right", 500);
    });


// //Select 2
//     $('.select-block').select2({
//         minimumResultsForSearch: Infinity,
//         theme: "classic"
//     });

//Bootstrap Tooltip
    $('[data-toggle="tooltip"]').tooltip();

//Bootstrap tabs

    // $('#rank-tabs a').click(function (e) {
    //     e.preventDefault();
    //     $(this).tab('show');
    // });



//PODMIANA KLASY PRZY SZEROKOŚCI OKNA 620PX DLA SEKCJI KATEGORIE

    var width = $(window).width();
    if (width < 500) {
        $("#infoSqueres .col-md-3").removeClass("col-xs-6").addClass("col-xs-12");
    }


});



//PODMIANA KLASY PRZY SZEROKOŚCI OKNA 620PX DLA SEKCJI KATEGORIE
$(window).resize(function () {

   var width = $(window).width();
   if (width < 500) {
       $("#infoSqueres .col-md-3").removeClass("col-xs-6").addClass("col-xs-12")
   }

   else {
       $("#infoSqueres .col-md-3").removeClass("col-xs-12").addClass("col-xs-6")
   }
});



//General vars for generating maps

var silesiaCenter = {lat: 50.207555, lng: 18.918350};
var worldCenter = {lat: 0.191, lng: 22.830};

var markEvent = {
    // url: "grafika/event_map_mark.png", // url
    url: url_event
};
var markStation = {
    url: url_station
};

var mapStyle = [
    {
        "featureType": "all",
        "elementType": "all",
        "stylers": [
            {
                "hue": "#ff0000"
            },
            {
                "saturation": -100
            },
            {
                "lightness": -30
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "color": "#ffffff"
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "color": "#353535"
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#656565"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#505050"
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#808080"
            }
        ]
    },
    {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#454545"
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "labels",
        "stylers": [
            {
                "hue": "#000000"
            },
            {
                "saturation": 100
            },
            {
                "lightness": -40
            },
            {
                "invert_lightness": true
            },
            {
                "gamma": 1.5
            }
        ]
    }
];


