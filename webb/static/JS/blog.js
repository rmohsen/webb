/**
 * Created by mohsen on 5/6/2017.
 */
// jQuery used
function loadDocs(token) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/posts",
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache",
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadDocs_count_offset(token,count,offset) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/posts?count="+count+"&offset="+offset,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache",
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadDocs_count(token,count) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/posts?count="+count,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache",
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadDocs_offset(token,offset) {
    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/posts?offset="+offset,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache",
            "postman-token": "af951ca8-7183-013a-f035-5ff9e54b258a"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function loadDoc_post_id(token, post_id) {

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/post?%20id="+post_id,
        "method": "GET",
        "headers": {
            "x-token": token,
            "cache-control": "no-cache",
            "postman-token": "dd3cc22d-850a-83f9-bd5f-6f2f604b2de7"
        }
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}

function postDoc(token, title, summary, text) {
    var form = new FormData();
    form.append("title", title);
    form.append("summary", summary);
    form.append("text", text);

    var settings = {
        "async": true,
        "crossDomain": true,
        "url": "http://ce419.herokuapp.com/blog/post",
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

