// Fetches a character name from Star wars API and displays it in
// <div#character> tag

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;
  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const name = data.name;
      $('#character').text(`${name}`);
    });
});
