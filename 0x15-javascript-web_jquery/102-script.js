// fetches and prints how to say “Hello” depending on the language
// uses the url https://www.fourtonfish.com/hellosalut/hello/ to fetch translations
$(document).ready(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
