$(document).ready(function () {
    $('#menuButton').click(function () {
      // Toggle class 'hidden' pada elemen menu untuk menampilkan/sembunyikan menu
      $('#menu').toggleClass('hidden');
  
      // Toggle class 'expanded' pada elemen menu untuk efek membesar
      $('#menu').toggleClass('expanded');
    });
  });