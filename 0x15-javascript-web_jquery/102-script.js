// Fetches and prints 'hello' depending on language input

const $ = window.$;

$(document).ready(() => {
  $('#btn_translate').click(() => {
    const code = $('#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${code}`;
    $.get(url, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
