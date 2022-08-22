import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'formatNer'
})
export class FormatNerPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    if(typeof value === 'string') {
      const regex = /\[(.*?)\]/g;
      value = value.replace(regex, '<b>[$1]</b>').replace(/(:.+?)\]/g, '<span class=\'entity\'>$1</span>]');
    }
    return value;
  }

}
