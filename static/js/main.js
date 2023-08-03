$(document).ready(function() {
    $('.ws-list li').mouseenter(function() {
        $(this).addClass('ws-lihover');
    });
    $('.ws-list li').mouseleave(function() {
        $(this).removeClass('ws-lihover');
    });
});