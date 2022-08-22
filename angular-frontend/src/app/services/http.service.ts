import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { map } from 'rxjs';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root',
})
export class HttpService {
  constructor(private http: HttpClient) {}

  getEntities(text: string, language: string, model: string) {
    return this.http
      .post<{ result: string }>(environment.nerURL, {
        text: text,
        model: model,
        language: language,
      })
      .pipe(map((response) => response.result));
  }

  getLanguages() {
    return this.http.get(environment.languageURL);
  }

  getLanguageModels(langauge: string) {
    const params = new HttpParams().set('language', langauge);
    return this.http.get(environment.modelURL, { params: params });
  }
}
