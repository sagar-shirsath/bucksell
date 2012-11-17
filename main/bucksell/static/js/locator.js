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

    var ilat = lat, ilong = long;
    var locations = [
        ['Item 1', 18.520163803962166, 73.8522221772156, 2],
        ['Item 2', 18.519349945198922, 73.8575007645569, 1],
        ['Item 2', 18.520123111115968, 73.85172865075685, 1],
        ['Item 2', 18.522178087747562, 73.85074159783937, 1],
        ['Item 2', 18.523622660500678, 73.85988256616213, 1],
        ['Item 2', 18.523887158415445, 73.86247894448854, 1],
        ['Item 2', 18.52350058440203, 73.86361620111086, 1],
        ['Item 2', 18.523724390516314, 73.84986183328249, 1],
        ['Item 2', 18.520774195493225, 73.84891769570925, 1],
        ['Item 2', 18.523276777994827, 73.84621402902224, 1],
        ['Item 2', 18.525514828885502, 73.85820886773683, 1],
        ['Item 2', 18.527061101480598, 73.85820886773683, 1],
        ['Item 2', 18.523643006508646, 73.84411117715456, 1],
        ['Item 2', 18.519858607379767, 73.84466907662966, 1]
    ];


    var latlng = new google.maps.LatLng(lat, long);
    var mapsOptions = {
        zoom:18,
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

//    google.maps.event.addListener(map, 'click', function (event) {
//        //call function to create marker
//        if (marker) {
//            marker.setMap(null);
//            marker = null;
//        }
//        console.log(event.latLng.Ya + ' ' + event.latLng.Za);
//        $('#id_latitude').val(event.latLng.Ya);
//        $('#id_longitude').val(event.latLng.Za);
//
//        var latlng1 = new google.maps.LatLng(event.latLng.Ya, event.latLng.Za);
//
//        geocoder.geocode({'latLng':latlng1}, function (results, status) {
//            if (status == google.maps.GeocoderStatus.OK) {
//                if (results[1]) {
//                    console.log('Address = ' + JSON.stringify(results[0]['formatted_address']));
//                    console.log('City = ' + JSON.stringify(results[0]['address_components'][2]['long_name']));
//                    console.log('State = ' + JSON.stringify(results[0]['address_components'][4]['long_name']));
//                    //                console.log(JSON.stringify(results[0]['address_components'][4]['short_name']));
//
//                    console.log('Country = ' + JSON.stringify(results[0]['address_components'][5]['long_name']));
////                console.log(JSON.stringify(results[0]['address_components'][5]['short_name']));
//
//                    $('#id_location').val(JSON.stringify(results[0]['formatted_address']));
//
//                }
//            }
//            else {
//                alert("Geocoder failed due to: " + status);
//            }
//        });
//
//        marker = createMarker(event.latLng, "name", "<b>Location</b><br>" + event.latLng, map);
//    });
    var myOptions = {
        disableAutoPan:false,
        maxWidth:0,
        alignBottom:true,
        pixelOffset:new google.maps.Size(-16, -11),
        zIndex:null,
        boxClass:"info-windows",
        closeBoxURL:"",
        pane:"floatPane",
        enableEventPropagation:false,
        infoBoxClearance:"10px"
    };
//    var infowindow = new google.maps.InfoWindow({
//        boxClass: "info-windows"
//    });
    var infowindow = new InfoBox(myOptions);

    var marker, i;

//    for (i = 0; i < locations.length; i++) {
//        marker = new google.maps.Marker({
//            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
//            animation: google.maps.Animation.DROP,
//            map: map,
//            title:locations[i][0]
//        });
//
//        google.maps.event.addListener(marker, 'click', (function(marker, i) {
//            return function() {
//                infowindow.setContent(locations[i][0]);
//                infowindow.open(map, marker);
//            }
//        })(marker, i));
//    }
    $.each($('input[type=hidden]'), function () {

        marker = new google.maps.Marker({
            position:new google.maps.LatLng($(this).attr('rel'), $(this).attr('rev')),
            animation:google.maps.Animation.DROP,
            map:map,
            title:$(this).attr('value')
        });
        var img_src = $(this).attr('id');
        var item_name = $(this).attr('value');
        var item_id = $(this).attr('item-id');
        var view_url = '/items/view/' + $(this).attr('item-slug');
        var price = $(this).attr('item-price');

        var myHtml = '<div style="text-align: center; text-overflow: ellipsis;overflow-x: hidden" id=' + item_id + '><a style="text-decoration: none" href=' + view_url + '><img src=' + img_src + ' height=90px width=90px/>' +
            '<span style="font-size: 18px;margin-top: 10px;margin-bottom: 10px">' + item_name + '<br><span style="font-size: 13px">Price : $'+price+'</span></a></div>';

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                $('#item_info').css('display','block');
                $('#item_name_detail').text(item_name);
                $('#item_image_detail').attr('src', img_src);
                infowindow.open(map, marker);
            }
        })(marker, i));

        google.maps.event.addListener(marker, 'mouseover', (function (marker, i) {
            return function () {
                infowindow.setContent(myHtml);
                infowindow.open(map, marker);
            }
        })(marker, i));

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
//                infowindow.setContent(myHtml);

                console.log($(infowindow.getContent()).attr('id'));

                var item_id = $(infowindow.getContent()).attr('id');

                $.ajax({
                    url:"/items/view_item_ajax/" + item_id,
                    success:function (responce) {

                        console.log(responce);

                        $('#item_img').attr('src', responce.item_photo_url);
                        $('#seller_img').attr('src', responce.seller_photo);
                        $('#item_name').text(responce.name);

                        $('#item_description').text(responce.description);

                    }
                });
                infowindow.open(map, marker);
            }
        })(marker, i));

//        console.log($(this).attr('value'));
//        console.log($(this).attr('rel'));
//        console.log($(this).attr('rev'));

    });
    var pinImage = new google.maps.MarkerImage("http://maps.google.com/mapfiles/ms/micons/homegardenbusiness.png");
    var marker = new google.maps.Marker({
        position:latlng,
        animation:google.maps.Animation.DROP,
        map:map,
        title:"Your location"
    });
//    console.log('http://'+location.hostname + ':8000/static/images/home.png');
    google.maps.event.addListener(marker, 'mouseover', function () {
//        infowindow.setContent("<h3>Your Location :)</h3>");
//        infowindow.open(map, marker);
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
