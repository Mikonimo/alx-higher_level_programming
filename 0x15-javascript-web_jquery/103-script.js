$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchTranslation () {
    const langCode = $('#language_code').val();

    // Fetch the translation from the API
    $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function (data) {
      $('#hello').text(data.hello);
    }).fail(function () {
      $('#hello').text('Error: Could not fetch translation');
    });
  }

  // Fetch translation when the button is clicked
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  // Fetch translation when Enter key is pressed in the input field
  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // 13 is the Enter key
      fetchTranslation();
      event.preventDefault(); // Prevent the default form submission
    }
  });
});
