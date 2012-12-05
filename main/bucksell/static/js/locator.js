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

    var infowindow = new InfoBox(myOptions);

    var marker, i;

    $.each($('input[type=hidden]'), function (index) {

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
            '<span style="font-size: 18px;margin-top: 10px;margin-bottom: 10px">' + item_name + '<br><span style="font-size: 13px;text-overflow: clip;white-space: nowrap">Price : $'+price+'</span></a></div>';

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
        google.maps.event.addListener(marker, 'mouseout', (function (marker, i) {
            return function () {
//                infowindow.setContent(myHtml);
                setTimeout(function(){
                    infowindow.close();
                },2000);
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
        if($(this).attr('first_item') == 'yes'){
           map.setCenter(new google.maps.LatLng($(this).attr('rel'), $(this).attr('rev')));
        }
        console.log(index);
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
//            alert("Geocoder failed due to: " + status);
        }
    });

}