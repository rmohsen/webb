/**
 * Created by mohsen on 5/7/2017.
 */

function loadComments(token, post_id) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/comments?post_id=" + post_id,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadComments_count_offset_post_id(token, count, offset, post_id) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/comments?post_id=" + post_id + "&count=" + count + "&offset=" + offset,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadComments_count_post_id(token, count, post_id) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/comments?post_id=" + post_id + "&count=" + count,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadComments_offset_post_id(token, offset, post_id) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/comments?post_id=" + post_id + "&offset=" + offset,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function postComment_post_id_text(token,post_id,text) {
    var form = new FormData();
    form.append("post_id", post_id);
    form.append("text", text);

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/comment",
        "method": "POST",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache"
        },
        "processData": false,
        "contentType": false,
        "mimeType": "multipart/form-data",
        "data": form
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

