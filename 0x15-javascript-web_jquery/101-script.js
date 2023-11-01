// Adds, removes and clears list items when respective tags are clicked

document.addEventListener('DOMContentLoaded', () => {
  const $ = window.$;

  const myList = $('ul.my_list');

  // Add item to unordered list
  const listItem = '<li>Item</li>';
  $('#add_item').click(() => { myList.append(listItem); });

  // Remove last item from list
  $('#remove_item').click(() => {
    const lastListItem = myList.children().last();
    lastListItem.remove();
  });

  // Clear the items in the list
  $('#clear_list').click(() => { myList.empty(); });
});
