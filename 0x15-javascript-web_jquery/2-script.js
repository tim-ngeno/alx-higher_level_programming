// Updates text color of <header> when <div#red_header> is clicked
document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;

  $('div#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
