// updates the text of the HTML tag header to "New Header!!!"
// when the user clicks on DIV#update_header
$(function () {
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
