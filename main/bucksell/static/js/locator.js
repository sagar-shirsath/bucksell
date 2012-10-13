var map = null;
var marker = null;

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(display_map, onErrorLocation, {timeout:3000});
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
    console.log(map);
    return marker;
}
//
//
function display_map(position){

    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
    var mapsOptions={
        zoom:10,
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
        marker = createMarker(event.latLng, "name", "<b>Location</b><br>"+event.latLng,map);
    });

    var marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: "User location"
    });

//
//    geocoder.geocode({'latLng': latlng}, function(results, status){
//        if (status == google.maps.GeocoderStatus.OK)
//        {
//            if (results[1])
//            {
//                console.log('Address = '+JSON.stringify(results[0]['formatted_address']));
//
//                console.log('City = '+JSON.stringify(results[0]['address_components'][2]['long_name']));
//
//                console.log('State = '+JSON.stringify(results[0]['address_components'][4]['long_name']));
////                console.log(JSON.stringify(results[0]['address_components'][4]['short_name']));
//
//                console.log('Country = '+JSON.stringify(results[0]['address_components'][5]['long_name']));
////                console.log(JSON.stringify(results[0]['address_components'][5]['short_name']));
//
//            }
//        }
//        else
//        {
//            alert("Geocoder failed due to: " + status);
//        }
//    });

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
