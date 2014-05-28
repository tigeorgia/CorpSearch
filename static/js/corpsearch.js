/**
 * Get cookie value by name
 * @param name Cookie name
 * @returns str Cookie value
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/**
 * Functions to run on pageload
 */
$(function () {

    /**
     * Change language
     */
    $(".lang-choose").click(function () {
        var loc = window.location.pathname;
        var current_lang = loc.split("/")[1];
        var new_lang = $(this).parent().attr('value');
        var next = "/" + loc.replace('/' + current_lang + '/', "");
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            url: "/" + current_lang + "/i18n/setlang/",
            type: 'post',
            data: {language: new_lang, next: next},
            headers: {'X-CSRFToken': getCookie('csrftoken')}
        }).done(function () {
            location.href = '/' + new_lang + next;
        });
    });

    /**
     *  Highlight current page in navigation
     */
    $(function (){
        var url = window.location.pathname;
        $('.navbar-nav a[href="'+ url +'"]').parent().addClass('active');
    });



});
