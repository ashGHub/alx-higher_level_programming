// fetches data from the URL https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
