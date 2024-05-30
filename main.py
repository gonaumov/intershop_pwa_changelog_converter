import ollama

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
prompt = f"""
For each occurrence of the pattern ## From [from version number] to [to version number], extract the entire text until the next ## marker.
Remember extracted text as [extracted text].
Rewrite [extracted text] from past simple or present perfect tense to future simple tense, for example:
"We removed" becomes "We will remove" and keep the whole text and text meaning. Just make it in future tense if there is need.
In [extracted text] find mentioning of Angular version. If there is no
Angular version take the one from previous row. If there is no previous row
take version 11 and remember it as [angular version].
In [extracted text] find mentioning of NodeJS version. If there is no
NodeJS version take the one from previous row. If there is no previous row
take version 14.15.0 LTS and remember it as [nodejs version].
In [extracted text] find mentioning of NPM version. If there is no
NPM version take the one from previous row. If there is no previous row
take version 6.14.8 and remember it as [npm version].
Finally output the following table. Please sort
the entire output table based on the values in the "From PWA version" column.
| From PWA version                      | To PWA version                     | Angular version                                                                  | NodeJS version                                                              | NPM version                                                              | Things we need to do                                  | Estimate                    |
|---------------------------------------|------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------|
| [from version number]                 | [to version  number]               | [angular version]                                                                | [nodejs version]                                                            | [npm version]                                                            | [extracted text]  - the whole text don't summarize it | 1 - this is hardcoded value |
|---------------------------------------|------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|-------------------------------------------------------|-----------------------------|
Here is the input data:
## From 2.2 to 2.3

The 'contact us' functionality has been moved into an extension and we have introduced the feature toggle `contactUs` in the `environment.model.ts` that is switched on by default.

The `getFilteredProducts` method has been moved from the `FilterService` to the `ProductsService`, since the `/products` API is used.
Together with this change, the default product attributes for product listings have been externalized and are easily overridable now.

With [#1135](https://github.com/intershop/intershop-pwa/pull/1135), the default model representation used by `NgbDatepicker` is the native ES6 `Date` now.
During this refactoring, the `DateHelper` class has been removed. **This will not concern you if you use `ish-date-picker-field` directly**.
However, if you use `NgbDatepicker` outside of formly, some helpers you might have used are gone.
Please use the underlying functions from `Date`, [`NgbCalendar`](https://ng-bootstrap.github.io/#/components/datepicker/api#NgbCalendar) and [`date-fns`](https://date-fns.org) directly, or create your own `DateHelper`.

## From 2.1 to 2.2

The PWA 2.2 contains an Angular update to version 13.3.0 and many other dependencies updates.<br/>
These updates required some internal webpack handling changes especially for the template overloading.<br/>
Also, some test adaptions where necessary, so is it now necessary to mock the `SwiperComponent`.<br/>
Another change is the [Formly](https://formly.dev/) downgrade from v6 pre-release to v5 that still works with Angular 13 with a changed `ngcc` setting.<br/>
After the updates, the deprecated RxJS MapTo operators (`mapTo`, `mergeMapTo`, `switchMapTo`) were replaced [Deprecating MapTo variants](https://github.com/ReactiveX/rxjs/issues/6399).
Linting will point out these issues in custom code that can easily be replaced then.

The Intershop PWA now uses Node.js 16 LTS with a corresponding npm version >=8.0.0.
With this new npm, calls using `npx npm-run-all` in CI have to be changed to `npm run exec npm-run-all`.

Changes with Angular 13 require to declare less dependencies in test beds than before.
For that reason the PWA 2.2 contains two pull requests that cleanup a lot of test specs (see #1057 and #1072).
It is not considered a breaking change but it might result in merge conflicts with customized Jest tests.
To cleanup the own code base run `npm run cleanup-testbed`.
Run `npm run cleanup-testbed -- --help` for more detailed options.

The `shared/formly` folder - containing all custom types, wrappers, etc - was updated.<br/>
For a cleaner separation of code artifacts, there are now multiple subfolders declaring their own modules where formly is partly configured.
The `FormlyModule` brings all these together, so you can use it just like before.
If you made any changes in `shared/formly`, you will have to adapt the corresponding modules.<br/>
Additionally, we introduced a `formly/field-library` subfolder that contains a `FieldLibrary` service which enables you to define reusable `FormlyFieldConfig`s and access them easily.
If you have customized anything in `shared/formly-address-forms/configurations/address-form-configuration.ts`, for example, the `standardFields` variable, you will have to migrate these changes by defining new `FieldLibraryConfiguration`s.
The address form configurations now use the new `FieldLibrary` functionality under the hood.<br/>
For more information, read the new [Field Library](../guides/field-library.md) documentation.

The compare products functionality was moved into an extension.
The already existing `compare` feature toggle works as before but the compare components integration changed to lazy components, e.g., `<ish-product-add-to-compare displayType="icon"></ish-product-add-to-compare>` to `<ish-lazy-product-add-to-compare displayType="icon"></ish-lazy-product-add-to-compare>`.
For other compare components, check the compare-exports.module.ts file.
"""


def main(prompt_text):
    print("Please wait ...")
    response = ollama.chat(model='intershop-changelog-converter', messages=[{'role': 'user', 'content': prompt_text}])
    with open('response.md', 'w') as file:
        file.write(response['message']['content'])
    print("All done!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(prompt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
