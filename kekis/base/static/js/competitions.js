
$(document).on('click', '.main-block__button', function() {
    $(this).addClass("main-block__button__liked").removeClass("main-block__button");
    const catid = $(this).attr("data-catid");
    const csrftoken = getCSRFToken();

    $.ajax({
        type: "POST",
        url: "/liked/",
        data: {
            'liked_id': catid
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
            console.log(data);
        }
    });
});


$(document).on('click', '.main-block__button__liked', function() {
    $(this).addClass("main-block__button").removeClass("main-block__button__liked");
    const catid = $(this).attr("data-catid");
    const csrftoken = getCSRFToken();

    $.ajax({
        type: "POST",
        url: "/unliked/",
        data: {
            'liked_id': catid
        },
        beforeSend: function(xhr) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        },
        success: function(data) {
        }
    });
});