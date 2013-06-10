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
                    var abils = $('#abilities');
                    _.defaults(data, {sub_types : "", power : "", toughness : "", cost : "", abilities : "", flavor_text : ""});
                    $('#card').html(cardTemplate({url: data.image_url, name: data.name, type: data.type,
                                                  sub_type: data.sub_types, power: data.power, toughness: data.toughness,
                                                  cost: data.cost, abilities: data.abilities, flavor_text: data.flavor_text,
                                                  illustrator: data.illustrator}));
                    cardblock.show();
                } else {
                    notfound.show();
                }
            });
    });
});
