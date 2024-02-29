$(document).ready(function () {
  const $addItem = $('div#add_item');
  const $removeItem = $('div#remove_item');
  const $clearList = $('div#clear_list');

  $addItem.on('click', function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $removeItem.on('click', function () {
    $('ul.my_list li:last-child').remove();
  });
  $clearList.on('click', function () {
    $('ul.my_list > li').remove();
  });
});
