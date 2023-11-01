/*
  adds the class `red` to the <header> element when the user clicks on
  the tag DIV#red_header
*/
document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;

  $('div#red_header').click(() => {
    $('header').addClass('red');
  });
});
