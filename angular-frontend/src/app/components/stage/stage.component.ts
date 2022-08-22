import { ChangeDetectionStrategy, Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-stage',
  templateUrl: './stage.component.html',
  styleUrls: ['./stage.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class StageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
