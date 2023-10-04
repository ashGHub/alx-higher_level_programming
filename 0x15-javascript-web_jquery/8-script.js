// fetches and lists all movies title by
// using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    const movies = data.results;
    for (const movie of movies) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  });
});
