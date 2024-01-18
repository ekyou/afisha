var cinemaHall1 = {
    row: [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
  },
  cinemaHallMap = '';
var rows = 1;
var count = 1;
var rowsHallMap = '';
var buyButton = document.querySelector(`#button-buy`);

$.each(cinemaHall1.row, function(row, numberOfSeats) {
  cinemaHallRow = '';
  rowsHallMap = '';
  for (i = 1; i <= numberOfSeats; i++) {
    cinemaHallRow += '<button class="seat" data-row="' +
      Number(rows) + '" data-seat="' +
      i + '" value="' + count +
       '">&nbsp;</button>';
    count += 1
  }
  rowsHallMap = '<div class="rows">' + rows + ' ряд</div>'
  cinemaHallMap += rowsHallMap + cinemaHallRow + rowsHallMap + '<div class="passageBetween">&nbsp;</div>';
  rows += 1;
});

$('.zal1').html(cinemaHallMap);

$('.seat').on('click', function() {
  $(this).toggleClass('bay').siblings().removeClass('bay');

  showBaySeat();
});

$('#id_place').addClass('input-style');
$('#id_concert').addClass('input-style');
$("#id_place").hide();
$("#id_concert").hide();

$('.seat').on('click', function(){
let a = $(this).attr("value");
let b = $(this).data().row + ' ряд ' + $(this).data().seat + ' место'
    $('#id_place').val(a).trigger('change');
    $('#select-or').text(b).trigger('change');
})
/*$(item).data().row + ' ряд ' + $(item).data().seat + ' место'*/
function showBaySeat() {
  result = '';
  $.each($('.seat.bay'), function(key, item) {
    result += '<div class="ticket">Ряд: ' +
      $(item).data().row + ' Место:' +
      $(item).data().seat + '</div>';
  });

  $('.result').html(result);
}




