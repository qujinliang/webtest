$(document).ready(function () {
    $('#btn').on('click',function () {
        $.get('/ajax',function(data) {
            $('#result').html(data);
        })
    });
});
$(document).ready(function () {
    $('#btn2').on('click',function () {
        $.post('/roomid',{roomid:$('#roomid').val()},function (data) {
            $('#result1').text(data);
        })
    });
});