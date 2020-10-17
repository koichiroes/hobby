"use strict";
class APIRequest {
    static get(path) {
        return $.ajax({
            method: 'GET',
            url: path,
        });
    }
    static post(path, data, contentType = 'application/json') {
        return $.ajax({
            method: 'POST',
            url: path,
            data: data,
            contentType: contentType,
        });
    }
}
const getDataFromForm = (id) => $(id).text();
const postToForm = () => {
    return APIRequest.post('/api/form/send', {
        name: getDataFromForm('#name'),
        email: getDataFromForm('#email'),
        company: getDataFromForm('#company'),
    }, 'application/x-www-form-urlencoded');
};
$('#register-form').on('submit', () => {
    postToForm()
        .done(_ => {
        $('#result').append('success to post');
    })
        .fail(_ => {
        $('#result').append('failed to post');
    });
    return false;
});
