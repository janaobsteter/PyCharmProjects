$('.launch-modal').on('click', function(e){
    e.preventDefault();
    $( '#' + $(this).data('modal-id') ).modal();
});


$('#myModal').on('shown.bs.modal', function () {
  $('#video1')[0].play();
})
$('#myModal').on('hidden.bs.modal', function () {
  $('#video1')[0].pause();
})