const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  $('div#hello').text(data.hello);
});
