import { api } from "@/services/core";

class GenericService {
  resourceUrl;
  needLookup;
  api;

  constructor(url) {
    this.resourceUrl = url;
    this.api = api;
  }

  getApiInstace() {
    return this.api;
  }

  getUrl() {
    return this.resourceUrl;
  }

  getQueryParams(query) {
    return Object.keys(query).reduce((acc, key) => {
      return acc + "&" + key + "=" + query[key];
    }, "?");
  }

  async index(query) {
    const response = await api.get(`${this.getUrl()}`, { params: query });
    return response.data;
  }

  async show(id) {
    const response = await api.get(`${this.getUrl()}${id}/`);
    return response.data;
  }

  async create(data, headers = {}) {
    const response = await api.post(`${this.getUrl()}`, data, { headers });
    return response.data;
  }

  async update(id, data) {
    const response = await api.put(`${this.getUrl()}${id}/`, data);
    return response.data;
  }

  async partialUpdate(id, data) {
    const response = await api.patch(`${this.getUrl()}${id}/`, data, {
      headers: { "X-CSRFToken": xcsrf },
    });
    return response.data;
  }

  async delete(id) {
    const response = await api.delete(`${this.getUrl()}${id}/`);
    return response.data;
  }
}

export default GenericService;
