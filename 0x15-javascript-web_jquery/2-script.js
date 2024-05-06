//JavaScript that updates text color of header to red tag DIV#red_header
$(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  });
});
