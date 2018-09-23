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

// var silesiaCenter = new google.maps.LatLng(59.243555, 19.995350);
// var worldCenter = new google.maps.LatLng(39.305, -76.617);

function initMap() {


    var locationStations = [
        ['Sosnowie [SOS] ',  -43.860600, 171.294639, 1 ],
        ['Mysłowice [MYS]',  35.319650, 137.252233, 2],
        ['Łaziska Górne [LAG]', -2.739081, 102.196058, 3],
        ['Chorzów [CHR]',  -29.993567, -71.010555, 4]
    ];


    var localMap = new google.maps.Map(document.getElementById('map'), {
        zoom: 10,
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
                        '<strong>Magnituda: </strong>'+locations[i][2] + '<br />'+
                        '<a class="text-right" href="'+locations[i][5]+'">Więcej</a>'+
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
                    '<a class="text-right" href="'+locationsWorld[i][5]+'">Więcej</a>'+
                    '</div>'

                );


                infowindow.open(worldMap, marker);
            }
        })(marker, i));
    }

}

