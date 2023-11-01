// Displays the value of 'hello' from a fetch response in the tag <div#hello>

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;
  fetch(url)
    .then((response) => { return response.json(); })
    .then((data) => {
      $('#hello').text(`${data.hello}`);
    });
});
