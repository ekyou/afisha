var afishes = 8;
var afishesRowAll = '';
var afishesRow = '';

for (i = 1; i <= afishes; i++) {
  afishesRow = '';
  afishesRow = '<div class="block-afisha"> <img src="static/main/image/masces-none.jpg" alt="" class="image-afisha-buy">' +
    '<div class="text-afisha-info">Название</div>' +
    '<div class="text-afisha-info">Цена</div>' +
    '&nbsp;</div>';
  afishesRowAll += afishesRow ;
};

$('.text-overlay').append(afishesRowAll);


