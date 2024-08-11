$(document).ready(function () {
  $('#btn_translate').click(function () {
    // Get the value from the input field
    const langCode = $('#language_code').val();

    // Fetch the translation from the API
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data) {
      // Update the div with the translated greeting
      $('#hello').text(data.hello);
    }).fail(function () {
      // Handle errors (e.g., invalid language code)
      $('#hello').text('Error: Could not fetch translation');
    });
  });
});
