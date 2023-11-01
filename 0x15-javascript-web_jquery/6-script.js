// Updates the text of <header> element to 'New Header!!!' when
// <div#update_header> is clicked
document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;
  const header = $('header');

  $('#update_header').click(() => {
    header.text('New Header!!!');
  });
});
