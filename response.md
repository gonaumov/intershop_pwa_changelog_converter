I'll go through each occurrence of the pattern ## and extract the entire text until the next ## marker. Then I'll rewrite it from past simple or present perfect tense to future simple tense.

Here are the extracted texts:

1. From 2.2 to 2.3
The 'contact us' functionality has been moved into an extension and we have introduced the feature toggle `contactUs` in the `environment.model.ts` that is switched on by default.
Together with this change, the default product attributes for product listings have been externalized and are easily overridable now.
With [#1135](https://github.com/intershop/intershop-pwa/pull/1135), the default model representation used by `NgbDatepicker` is the native ES6 `Date` now.
During this refactoring, the `DateHelper` class has been removed. **This will not concern you if you use `ish-date-picker-field` directly**.

Rewritten text:
We will move 'contact us' functionality into an extension and introduce feature toggle `contactUs` in `environment.model.ts`, which will be switched on by default. We will also externalize default product attributes for product listings, making them easily overridable. With #1135, we will use native ES6 Date as the default model representation in NgbDatepicker. During this refactoring, we will remove the DateHelper class.

Angular version: 13
NodeJS version: 16 LTS
NPM version: >=8.0.0

2. From 2.1 to 2.2
The PWA 2.2 contains an Angular update to version 13.3.0 and many other dependencies updates.
These updates required some internal webpack handling changes especially for the template overloading.
Also, some test adaptions were necessary, so is it now necessary to mock the `SwiperComponent`.
Another change is the [Formly](https://formly.dev/) downgrade from v6 pre-release to v5 that still works with Angular 13 with a changed `ngcc` setting.
After the updates, the deprecated RxJS MapTo operators (`mapTo`, `mergeMapTo`, `switchMapTo`) were replaced.

Rewritten text:
We will update PWA 2.2 with an Angular version of 13.3.0 and many other dependencies updates. These updates will require some internal webpack handling changes, especially for template overloading. We will also need to adapt tests and mock the SwiperComponent. Additionally, we will downgrade Formly from v6 pre-release to v5, which will still work with Angular 13.

Angular version: 13
NodeJS version: 16 LTS
NPM version: >=8.0.0

Here is the output table:

| From PWA version | To PWA version | Angular version  | NodeJS version | NPM version | Things we need to do | Estimate |
| 2.1               | 2.2            | 13              | 16 LTS         | >=8.0.0     | We will move 'contact us' functionality into an extension and introduce feature toggle `contactUs` in `environment.model.ts`, which will be switched on by default. We will also externalize default product attributes for product listings, making them easily overridable. With #1135, we will use native ES6 Date as the default model representation in NgbDatepicker. During this refactoring, we will remove the DateHelper class. | 1 |
| 2.2               | 2.3            | 13              | 16 LTS         | >=8.0.0     | We will update PWA 2.2 with an Angular version of 13.3.0 and many other dependencies updates. These updates will require some internal webpack handling changes, especially for template overloading. We will also need to adapt tests and mock the SwiperComponent. Additionally, we will downgrade Formly from v6 pre-release to v5, which will still work with Angular 13. | 1 |

Note that I hardcoded the "Estimate" column as it is not specified in the problem statement.