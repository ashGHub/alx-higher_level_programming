// fetches and prints how to say “Hello” depending on the language
// uses the url https://www.fourtonfish.com/hellosalut/hello/ to fetch translations
function translate () {
  const lang = $('INPUT#language_code').val();
  $.getJSON(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
    $('DIV#hello').text(data.hello);
  });
}

$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    translate();
  });
  $('INPUT#language_code').keypress((e) => {
    // if Enter key was pressed
    if (e.which === 13) {
      translate();
    }
  });
});
