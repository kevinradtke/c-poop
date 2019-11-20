import FetchHttpClient, { header, json, form } from "fetch-http-client";

export default class API {
  static call(options) {
    // Default options
    const op = {
      // url:"https://api.vitau.mx",
      // url: "https://api-test.vitau.mx",
      url: "http://127.0.0.1:5000",
      method: "get",
      service: "",
      params: "",
      tokenType: "Bearer",
      success(response) {},
      error(response) {},
      credentials: true,
      contentType: "form",
      multipart: false
    };

    // Replacing default options
    for (const key in options) {
      op[key] = options[key];
    }

    // Creatign a new client
    const client = new FetchHttpClient(op.url);

    // Content-Type: application/json
    client.addMiddleware(form());
    client.addMiddleware(json());
    if (op.credentials) {
      client.addMiddleware(
        header({
          Authorization: `${op.tokenType} ${localStorage.getItem("token")}`
        })
      );
    }

    const params = {};
    if (op.multipart) {
      const formData = new FormData();

      for (const k in op.params) {
        if (op.params.hasOwnProperty(k)) {
          formData.append(k, op.params[k]);
        }
      }
      params.body = formData;
    } else {
      params[op.contentType] = op.params;
    }

    // Performing the request
    client[op.method](op.service, params).then(response =>
      response.text().then(text => op.success(text))
    );
  }
}
