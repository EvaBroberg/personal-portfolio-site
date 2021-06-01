//read more

$('#toggle').click(function () {
    var elem = $('#toggle').text();
    if (elem == 'Read More') {
      //Stuff to do when btn is in the read more state
      $('#toggle').text('Read Less');
      $('#text').slideDown();
    } else {
      //Stuff to do when btn is in the read less state
      $('#toggle').text('Read More');
      $('#text').slideUp();
    }
  });

  $(window).scroll(function() {
    if ($(this).scrollTop() > 0) {
      $('.arrow-wrapper').fadeOut();
    } else {
      $('.arrow-wrapper').fadeIn();
    }
  });