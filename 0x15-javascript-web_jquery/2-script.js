// updates the text color of the header element to red
// when the user clicks on the tag DIV#red_header
$(function ()
{
  $('DIV#red_header').click(function () {
    $('header').css('color', 'red');
  });
});
