// $(document).ready(function () {
//
//     //Bootstrap karuzela
//     //  $("#myCarousel").carousel({
//     //      interval: 9000,
//     //      pause: "hover"
//     //  });
//
//
// });


//Google maps  fo home page

// var silesiaCenter = new google.maps.LatLng(50.243555, 18.995350);
// var worldCenter = new google.maps.LatLng(39.305, -76.617);

function initMap() {

    var locations = [
        ['Bytom', '12 listopad 2017 00:55', 3.1, 50.366495, 18.874169, 4],
        ['Orzesze', '6 listopad 2017 12:55', 2.1, 50.143555, 18.795350, 5],
        ['Katowice', '2 listopad 2017 07:55', 2.6, 50.243555, 18.995350, 3],
        ['Pszczyna', '30 listopad 2017 18:55', 2.8, 49.970026, 19.092426, 2],
        ['Lędziny', '5 grudzień 2017 03:55', 2.0, 50.130933, 19.142082, 1]
    ];

    var locationsWorld = [
        ['Nowa Zelandia', '12 listopad 2017 00:55', 6.1, -43.860600, 171.294639, 4],
        ['Japonia', '6 listopad 2017 12:55', 5.7, 35.319650, 137.252233, 5],
        ['Indonezja', '2 listopad 2017 07:55', 5.6, -2.739081, 102.196058, 3],
        ['Chile', '30 listopad 2017 18:55', 7.1, -29.993567, -71.010555, 2],
        ['Dominikana', '5 grudzień 2017 03:55', 6.5, 19.146026, -71.184710, 1],
        ['Włochy', '5 grudzień 2017 03:55', 5.5, 42.762221, 12.999896, 1],
        ['Grecja', '5 grudzień 2017 03:55', 4.7, 38.324176, 22.010317, 1]
    ];


    var locationStations = [
        ['Sosnowie [SOS] ',  -43.860600, 171.294639, 1 ],
        ['Mysłowice [MYS]',  35.319650, 137.252233, 2],
        ['Łaziska Górne [LAG]', -2.739081, 102.196058, 3],
        ['Chorzów [CHR]',  -29.993567, -71.010555, 4]
    ];


    var localMap = new google.maps.Map(document.getElementById('map'), {
        zoom: 9,
        center: silesiaCenter,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: mapStyle

    });

    var worldMap = new google.maps.Map(document.getElementById('map2'), {
        zoom: 2,
        center: worldCenter,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        styles: mapStyle
    });

    // var stationdMap = new google.maps.Map(document.getElementById('stationMap'), {
    //     zoom: 9,
    //     center: silesiaCenter,
    //     mapTypeId: google.maps.MapTypeId.ROADMAP,
    //     styles: mapStyle
    // });


    var infowindow = new google.maps.InfoWindow();

    var marker, i;
    var markers = [];

    //Markers Local Loop
    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][3], locations[i][4]),
            map: localMap,
            icon: markEvent
        });

        markers.push(marker);

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(
                    '<div class="markerDescription">'+
                        '<strong>Miasto: </strong>'+locations[i][0] + '<br />'+
                        '<strong>Czas: </strong>'+locations[i][1] + '<br />'+
                        '<strong>Energia: </strong>'+locations[i][2] + '<br />'+
                        '<a class="text-right" href="#">Więcej</a>'+
                    '</div>'

                );


                infowindow.open(localMap, marker);
            }
        })(marker, i));
    }


    //Markers World Loop
    for (i = 0; i < locationsWorld.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locationsWorld[i][3], locationsWorld[i][4]),
            map: worldMap,
            icon: markEvent
        });

        markers.push(marker);

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(
                    '<div class="markerDescription">'+
                    '<strong>Kraj: </strong>'+locationsWorld[i][0] + '<br />'+
                    '<strong>Czas: </strong>'+locationsWorld[i][1] + '<br />'+
                    '<strong>Magnituda: </strong>'+locationsWorld[i][2] + '<br />'+
                    '<a class="text-right" href="#">Więcej</a>'+
                    '</div>'

                );


                infowindow.open(worldMap, marker);
            }
        })(marker, i));
    }

}

