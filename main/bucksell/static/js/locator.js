var map = null;
var marker = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(display_map, onErrorLocation, {timeout:30000});
    }
    else {
        alert('Error detecting your location');
    }
}

function onErrorLocation(error){
    if(error.code == 1){
        alert('We are unable to detect your location!! Please change your browser location permission to allow for this site.');
    }
    else{
        alert('Unable to detect your location');
    }
}
var infowindow = new google.maps.InfoWindow({
        size: new google.maps.Size(150,50)
});
function createMarker(latlng, name, html,map) {

    var contentString = html;
    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        zIndex: Math.round(latlng.lat()*-100000)<<5
    });

    google.maps.event.addListener(marker, 'click', function() {
//        infowindow.setContent("Location");
        infowindow.open(map,marker);
    });
    google.maps.event.trigger(marker, 'click');

    return marker;
}
//
//
function display_map(position){

    geocoder = new google.maps.Geocoder();
    $('#id_latitude').val(position.coords.latitude);
    $('#id_longitude').val(position.coords.longitude);

    var ilat = position.coords.latitude, ilong = position.coords.longitude;
    var locations = [
        ['Item 1', 18.520163803962166,73.8522221772156,2],
        ['Item 2', 18.519349945198922, 73.8575007645569,1],
        ['Item 2', 18.520123111115968, 73.85172865075685,1],
        ['Item 2', 18.522178087747562, 73.85074159783937,1],
        ['Item 2', 18.523622660500678, 73.85988256616213,1],
        ['Item 2', 18.523887158415445, 73.86247894448854,1],
        ['Item 2', 18.52350058440203, 73.86361620111086,1],
        ['Item 2', 18.523724390516314, 73.84986183328249,1],
        ['Item 2', 18.520774195493225, 73.84891769570925,1],
        ['Item 2', 18.523276777994827, 73.84621402902224,1],
        ['Item 2', 18.525514828885502, 73.85820886773683,1],
        ['Item 2', 18.527061101480598, 73.85820886773683,1],
        ['Item 2', 18.523643006508646, 73.84411117715456,1],
        ['Item 2', 18.519858607379767, 73.84466907662966,1]
    ];


    var latlng = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
    var mapsOptions={
        zoom:16,
        center: new google.maps.LatLng(position.coords.latitude,position.coords.longitude),
        mapTypeControl: true,
        mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
        navigationControl: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    var map=new google.maps.Map(document.getElementById('map_canvas'), mapsOptions);

    google.maps.event.addListener(map, 'click', function() {
        infowindow.close();
    });

    google.maps.event.addListener(map, 'click', function(event) {
        //call function to create marker
        if (marker) {
            marker.setMap(null);
            marker = null;
        }
        console.log(event.latLng.Xa+' '+event.latLng.Ya);
        $('#id_latitude').val(event.latLng.Xa);
        $('#id_longitude').val(event.latLng.Ya);
        marker = createMarker(event.latLng, "name", "<b>Location</b><br>"+event.latLng,map);
    });

    var infowindow = new google.maps.InfoWindow();

    var marker, i;

    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            animation: google.maps.Animation.DROP,
            map: map,
            title:locations[i][0]
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }

    var marker = new google.maps.Marker({
        position: latlng,
        animation: google.maps.Animation.DROP,
        map: map,
        title: "User location"
    });

    geocoder.geocode({'latLng': latlng}, function(results, status){
        if (status == google.maps.GeocoderStatus.OK)
        {
            if (results[1])
            {
                console.log('Address = '+JSON.stringify(results[0]['formatted_address']));

                console.log('City = '+JSON.stringify(results[0]['address_components'][2]['long_name']));

                console.log('State = '+JSON.stringify(results[0]['address_components'][4]['long_name']));
//                console.log(JSON.stringify(results[0]['address_components'][4]['short_name']));

                console.log('Country = '+JSON.stringify(results[0]['address_components'][5]['long_name']));
//                console.log(JSON.stringify(results[0]['address_components'][5]['short_name']));

            }
        }
        else
        {
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
