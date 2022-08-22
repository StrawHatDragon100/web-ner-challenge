import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Observable } from 'rxjs';
import { HttpService } from 'src/app/services/http.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class FormComponent implements OnInit {

  myForm!: FormGroup;
  result$!: Observable<string>;
  languages$!: Observable<any>;
  models$!: Observable<any>;

  constructor(private fb: FormBuilder, private httpService: HttpService) { }

  ngOnInit(): void {
    this.myForm = this.fb.group({
      'text': '',
      'language': '',
      'model': ''
    });
    this.languages$ = this.httpService.getLanguages();
  }

  onSubmit() {
    this.result$ = this.httpService.getEntities(this.myForm.get('text')?.value, this.myForm.get('language')?.value, this.myForm.get('model')?.value);
  }

  onLanguageSelection() {
    this.models$ = this.httpService.getLanguageModels(this.myForm.get('language')?.value);
  }

}
