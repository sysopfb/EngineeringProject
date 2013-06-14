$(function() {
    var cardblock = $('#card');
    var notfound = $('#notfoundmsg');
    notfound.hide();
    $('#SearchButton').on('click', function() {
        $.getJSON($SCRIPT_ROOT + "/_get_card", {
            cardname: $('#search_card').val()
            }).done(function(data) {
                cardblock.hide();
                notfound.hide();
                var cardTemplate = _.template($('#card-template').html());
                if(data.found) {
                    //Defaults so we don't have any null values show up
                    _.defaults(data, {sub_types : "", power : "", toughness : "", cost : "", abilities : "", flavor_text : ""});
                    //This changes the cost values into {} style
                    // for ease of conversion later
                    var newCOST = data.cost.replace(/([0-9]+)|(.+?)/g, '{$1}');
                    $('#card').html(cardTemplate({url: data.image_url, name: data.name, type: data.type,
                                                  sub_type: data.sub_types, power: data.power, toughness: data.toughness,
                                                  cost: newCOST, abilities: data.abilities, flavor_text: data.flavor_text,
                                                  illustrator: data.illustrator}));
                    //Easy way to change {} values to images
                    var newHTML = $('#card').html().replace(/\{(.+?)\}/g, '<img src=static/images/$1.png>');
                    $('#card').html(newHTML);
                    cardblock.show();
                } else {
                    notfound.show();
                }
            });
    });
});
