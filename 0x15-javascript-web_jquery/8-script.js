// Fetches and lists all movie titles from Star Wars API in the tag
// <ul#list_movies>

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;
  fetch(url)
    .then((response) => { return response.json(); })
    .then((data) => {
      for (const item of data.results) {
        const listItem = $(`<li>${item.title}</li>`);
        $('#list_movies').append(listItem);
      }
    });
});
