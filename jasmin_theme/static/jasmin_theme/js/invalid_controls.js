// Make sure the has-error class gets applied to the parent form-group of any invalid controls
$('.form-control:invalid').closest('.form-group').each(function() {
    $(this).addClass('has-error');
});
$(document).on('input', '.form-control', function(e) {
    var action = this.checkValidity() ? 'removeClass' : 'addClass';
    $(this).closest('.form-group').each(function() { $(this)[action]('has-error'); });
});
