var map = null;
var marker = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(display_my_map, onErrorLocation, {timeout:30000});
    }
    else {
//        alert('Error detecting your location');
        display_map(geoip_latitude(),geoip_longitude());
    }
}

function onErrorLocation(error) {

//        alert('Unable to detect your location');
        display_map(geoip_latitude(),geoip_longitude());

}
var infowindow = new google.maps.InfoWindow({
    size:new google.maps.Size(150, 50)
});
function createMarker(latlng, name, html, map) {

    var contentString = html;
    var marker = new google.maps.Marker({
        position:latlng,
        map:map,
        zIndex:Math.round(latlng.lat() * -100000) << 5
    });

    google.maps.event.addListener(marker, 'click', function () {
//        infowindow.setContent("Location");
        infowindow.open(map, marker);
    });
    google.maps.event.trigger(marker, 'click');

    return marker;
}
//
//
function display_my_map(position){
    display_map(position.coords.latitude,position.coords.longitude)
}
function display_map(lat,long) {

    geocoder = new google.maps.Geocoder();
    $('#id_latitude').val(lat);
    $('#id_longitude').val(long);


    var latlng = new google.maps.LatLng(lat, long);
    var mapsOptions = {
        zoom:16,
        center:new google.maps.LatLng(lat, long),
        mapTypeControl:true,
        mapTypeControlOptions:{style:google.maps.MapTypeControlStyle.DROPDOWN_MENU},
        navigationControl:true,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    }

    var map = new google.maps.Map(document.getElementById('map_canvas'), mapsOptions);

    google.maps.event.addListener(map, 'click', function () {
        infowindow.close();
    });

    google.maps.event.addListener(map, 'click', function (event) {
        //call function to create marker
        if (marker) {
            marker.setMap(null);
            marker = null;
        }
        console.log(event.latLng.Ya + ' ' + event.latLng.Za);
        $('#id_latitude').val(event.latLng.Ya);
        $('#id_longitude').val(event.latLng.Za);

        var latlng1 = new google.maps.LatLng(event.latLng.Ya, event.latLng.Za);

        geocoder.geocode({'latLng':latlng1}, function (results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[1]) {
                    console.log('Address = ' + JSON.stringify(results[0]['formatted_address']));
                    console.log('City = ' + JSON.stringify(results[0]['address_components'][2]['long_name']));
                    console.log('State = ' + JSON.stringify(results[0]['address_components'][4]['long_name']));
                    //                console.log(JSON.stringify(results[0]['address_components'][4]['short_name']));

                    console.log('Country = ' + JSON.stringify(results[0]['address_components'][5]['long_name']));
//                console.log(JSON.stringify(results[0]['address_components'][5]['short_name']));

                    $('#id_location').val(JSON.stringify(results[0]['formatted_address']));

                }
            }
            else {
                alert("Geocoder failed due to: " + status);
            }
        });

        marker = createMarker(event.latLng, "name", "<b>Location</b><br>" + event.latLng, map);
    });

    var marker = new google.maps.Marker({
        position:latlng,
        animation:google.maps.Animation.DROP,
        map:map,
        title:"Your location"
    });


    geocoder.geocode({'latLng':latlng}, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            if (results[1]) {
                console.log('Address = ' + JSON.stringify(results[0]['formatted_address']));

                console.log('City = ' + JSON.stringify(results[0]['address_components'][2]['long_name']));

                console.log('State = ' + JSON.stringify(results[0]['address_components'][4]['long_name']));
//                console.log(JSON.stringify(results[0]['address_components'][4]['short_name']));

                console.log('Country = ' + JSON.stringify(results[0]['address_components'][5]['long_name']));
//                console.log(JSON.stringify(results[0]['address_components'][5]['short_name']));
                $('#id_location').val(JSON.stringify(results[0]['formatted_address']));
            }
        }
        else {
            alert("Geocoder failed due to: " + status);
        }
    });

}


//var map = null;
//var marker = null;
//
//var infowindow = new google.maps.InfoWindow(
//    {
//        size: new google.maps.Size(150,50)
//    });
//
//// A function to create the marker and set up the event window function
//function createMarker(latlng, name, html) {
//    var contentString = html;
//    var marker = new google.maps.Marker({
//        position: latlng,
//        map: map,
//        zIndex: Math.round(latlng.lat()*-100000)<<5
//    });
//
//    google.maps.event.addListener(marker, 'click', function() {
//        infowindow.setContent(contentString);
//        infowindow.open(map,marker);
//    });
//    google.maps.event.trigger(marker, 'click');
//    return marker;
//}
//
//
//
//function initialize() {
//    // create the map
//    var myOptions = {
//        zoom: 8,
//        center: new google.maps.LatLng(43.907787,-79.359741),
//        mapTypeControl: true,
//        mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
//        navigationControl: true,
//        mapTypeId: google.maps.MapTypeId.ROADMAP
//    }
//    map = new google.maps.Map(document.getElementById("map_canvas"),
//        myOptions);
//
//    google.maps.event.addListener(map, 'click', function() {
//        infowindow.close();
//    });
//
//    google.maps.event.addListener(map, 'click', function(event) {
//        //call function to create marker
//        if (marker) {
//            marker.setMap(null);
//            marker = null;
//        }
//        marker = createMarker(event.latLng, "name", "<b>Location</b><br>"+event.latLng);
//    });
//
//}
