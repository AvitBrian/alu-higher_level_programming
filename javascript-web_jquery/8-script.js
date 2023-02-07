#!/usr/bin/node
$(document).ready(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    const results = data.results;
    for (const char of results) {
      $('UL#list_movies').append('<li>' + char.title + '</li>');
    }
  });
});
