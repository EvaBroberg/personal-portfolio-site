// hamburger menu

$('#hamburger').on('click', function () {
    $('.line1').toggleClass('closed1');
    $('.line2').toggleClass('closed2');
    $('.line3').toggleClass('closed3');
  });



$('.main-nav-item').on('click', function(){
  $(this).addClass('active').siblings().removeClass('active');
});

