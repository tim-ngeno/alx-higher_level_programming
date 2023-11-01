// Adds a list element to a list when `div#add_item` is clicked

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;

  $('#add_item').click(() => {
    const listItem = $('<li>Item</li>');
    $('ul.my_list').append(listItem);
  });
});
