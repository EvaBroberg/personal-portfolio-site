$(document).ready(function () {
    //INIT SIDENAV
    $('.button-collapse').sideNav();

    //INIT SCROLLSPY
    $('.scrollspy').scrollSpy();

    //INIT MODAL
    $('.modal').modal();

    //Scrollfire
    const options = [
      {
        selector: '.row-0',
        offset: 100,
        callback: function (el) {
          Materialize.fadeInImage($(el));
        },
      },
      {
        selector: '.row-1',
        offset: 50,
        callback: function (el) {
          Materialize.fadeInImage($(el));
        },
      },
      {
        selector: '.row-2',
        offset: 300,
        callback: function (el) {
          Materialize.fadeInImage($(el));
        },
      },
      {
        selector: '.row-3',
        offset: 400,
        callback: function (el) {
          Materialize.fadeInImage($(el));
        },
      },
      {
        selector: '.row-4',
        offset: 470,
        callback: function (el) {
          Materialize.fadeInImage($(el));
        },
      },
    ];

    $(window).scroll(function () {
      if (window.pageYOffset > 1000 - $(window).height()) {
        $('nav').removeClass('transparent').addClass('black-nav');
        console.log('halloo');
      } else {
        $('nav').addClass('transparent').removeClass('black-nav');
      }
    });

    Materialize.scrollFire(options);
  });