import { AbstractControl, ValidatorFn } from '@angular/forms';

export function imageValdatore(nameRe: RegExp): ValidatorFn {
    return (control: AbstractControl): { [key: string]: any } | null => {
        // tslint:disable-next-line:no-debugger
        debugger;
        const forbidden = nameRe.test(control.value);
        return forbidden ? { 'forbiddenName': { value: control.value } } : null;
    };
}
