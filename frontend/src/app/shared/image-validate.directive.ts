import { Directive } from '@angular/core';
import { Validator, NG_VALIDATORS, FormControl } from '@angular/forms';
import { AbstractControl, ValidatorFn } from '@angular/forms';

// validation function
function validateImageFactory(): ValidatorFn {
    return (c: AbstractControl) => {
        // tslint:disable-next-line:no-debugger
        debugger;
        let isValid = c.value === 'Juri';

        if (isValid) {
            return null;
        } else {
            return {
                juriName: {
                    valid: false
                }
            };
        }
    };
}

@Directive({
    // tslint:disable-next-line:directive-selector
    selector: '[isImage]',
    providers: [
        { provide: NG_VALIDATORS, useExisting: ImgaeValidatorDirective, multi: true }
    ]
})
export class ImgaeValidatorDirective implements Validator {

    validator: ValidatorFn;

    constructor() {
        // tslint:disable-next-line:no-debugger
        debugger;
        this.validator = validateImageFactory();
    }

    validate(c: FormControl) {
        // tslint:disable-next-line:no-debugger
        debugger;
        return this.validator(c);
    }
}