// toggles the class of the HTML tag header to red (#FF0000)
// when the user clicks on the tag DIV#toggle_header
$(function () {
  $('DIV#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
