class APIRequest {
  static get(path: string): JQuery.jqXHR<any> {
    return $.ajax({
      method: "GET",
      url: path,
    });
  }

  static post(
    path: string,
    data: { [key: string]: any } | string,
    contentType: string = "application/json"
  ): JQuery.jqXHR<any> {
    return $.ajax({
      method: "POST",
      url: path,
      data: data,
      contentType: contentType,
    });
  }
}

const getDataFromForm = (id: string): string => $(id).text();

const postToForm = () => {
  return APIRequest.post(
    "/api/form/send",
    {
      name: getDataFromForm("#name"),
      email: getDataFromForm("#email"),
      company: getDataFromForm("#company"),
    },
    "application/x-www-form-urlencoded"
  );
};

$("#register-form").on("submit", () => {
  postToForm()
    .done((_) => {
      $("#result").append("success to post");
    })
    .fail((_) => {
      $("#result").append("failed to post");
    });
  return false;
});
