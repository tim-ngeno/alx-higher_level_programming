// Toggles <header> class to red or green when user clicks on
// 'div#toggle_header' tag

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;
  const header = $('header');

  $('#toggle_header').click(() => {
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
