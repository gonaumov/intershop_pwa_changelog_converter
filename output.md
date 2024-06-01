| From PWA version | To PWA version | Angular version | NodeJS version | NPM version | Things we need to do | Estimate | Regression |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.26 | 0.27 | 11 | 14.15.0 LTS | 6.14.8 | We upgraded Cypress from Version 4 to 6 and followed all migrations in their [Migration Guide](https://docs.cypress.io/guides/references/migration-guide).

We have introduced a [Context Facade](../concepts/state-management.md#context-facades) for product entities and [refactored](https://github.com/intershop/intershop-pwa/pull/403) most of the components that are specific to a single product.
This includes:

- Targeted components no longer require a `product` input, as they retrieve the product from the context.
- The handling for adding products to the basket was refactored and simplified.
- Product quantity handling moved almost completely to the context.
- The decision for displaying certain components on product tiles and rows also moved into the context. | 1 | two days |
| 0.27 | 0.28 | 11 | 14.15.0 LTS | 6.14.8 | We removed the property `production` from Angular CLI `environment.ts` files.
Production mode can consistently be set by using Angular CLI configurations now.
This also works when running multiple configurations like `--configuration=brand,production`.

We removed the property `serviceWorker` from Angular CLI `environment.ts` files.
The Service Worker can now be set consistently depending on the current configuration in the `angular.json` file.

We removed the dependency to `ngx-swiper-wrapper` as it will [no longer be supported](https://github.com/zefoy/ngx-swiper-wrapper#eol-notice) and `swiper` itself now [natively supports](https://swiperjs.com/angular) Angular (see changes #552).

We introduced [formly](https://formly.dev/) to handle all kinds of forms from now on.
We removed `src/app/shared/address-forms` in favor of `src/app/shared/formly-address-forms` and `src/app/shared/forms-dynamic` in favor of a generalized formly integration in `src/app/shared/formly`.
To implement your country-specific address forms in formly, see [Forms](./forms.md#the-address-form-as-an-example-of-a-reusable-form).

We introduced an improved usage of memoized selectors for product selectors, split up state, saved additionally retrieved data in separate places, and migrated almost all product-related components to use the previously introduced product context facade (see changes #528). | 1 | two days |
| 0.28 | 0.29 | 11 | 14.15.0 LTS | 6.14.8 | We activated TypeScript's [`noImplicitAny`](https://www.typescriptlang.org/tsconfig#noImplicitAny).
Please refer to the [Type Safety](./getting-started.md#type-safety) part in the Getting Started Guide for motivations. | 1 | two days |
| 0.29 | 0.30 | 11 | 14.15.0 LTS | 6.14.8 | We introduced the feature toggle 'guestCheckout' in the `environment.model.ts`.

We switched to encode user logins when used in the api service.
This is to enable special characters (like the #) that are sometimes present in user logins (SSO case!) but would have led to errors before. | 1 | two days |
| 0.31 | 1.0 | 11 | 14.15.0 LTS | 6.14.8 | The Angular configuration mechanism of the Intershop PWA was refactored to support running multiple configurations in one Docker image (see [Guide - Multiple Themes](./themes.md)).
This now means that the former `environment.local.ts` which had a standalone configuration can no longer be supported.
Instead, theme-specific environments exist for `default` and `blue`, and development settings can be overridden in `environment.development.ts`, which are imported into the theme-specific configurations (see [Guide - Development](./development.md#development-server)).
`npm install` will create an initial version of the `environment.development.ts` that can be filled with the needed information from `environment.local.ts`.
The `environment.local.ts` itself becomes obsolete and can be deleted.

Locale definitions in `environment.ts` models are no longer supported, only ICM channel configurations are now used for switching locales. | 1 | two days |
| 1.1 | 1.2 | 11 | 14.15.0 LTS | 6.14.8 | The `dist` folder now only contains results of the build process (except for `healthcheck.js`).
You must **not** edit any file inside that `dist` folder, since this would include not being able to change Kubernetes liveness or readiness probes we included SSR container related source code under `src/ssr/server-scripts/` | 1 | two days |
| 1.4 | 2.0 | 11 | 14.15.0 LTS | 6.14.8 | Since [TSLint has been deprecated](https://blog.palantir.com/tslint-in-2019-1a144c2317a9) for a while now, and Angular removed the TSLint support, we had to migrate our project from TSLint to ESLint as well.
This means in version 2.0 all TSLint rules and configurations were removed and replaced by ESLint where possible.

This not only required configuration changes in the Intershop PWA project but also application code adaptions to comply with some of the new ESLint rules.
To allow for an as easy as possible migration of existing PWA projects, we split the whole switch in separate commits that should make it easier to resolve potential merge conflicts by providing some context, e.g., changes to satisfy a specific rule or project configuration changes etc.
We advise you to first cherry pick all the `eslint` commits provided by the PWA release before applying the lint rules to the project customizations to fix the issues that reside in the project code.
If the found issues are too many to address them in an ordered manner, it is probably best to temporarily disable some of the failing rules in `.eslintrc.json` (see [Configuring ESLint](./eslint.md#configuring-eslint) and to only fix one after another.

It is also probably a good idea to do the PWA 2.0 migration not in one go as described in [Import Changes from New PWA Release](./customizations.md#import-changes-from-new-pwa-release-migration) but to first do the commits before the linter switch and bring your project to a clean state (`npm run check`).
After this, all the linter switch commits should be applied and the project should be brought back to a clean state.
Once this is done, subsequent commits should be migrated.
If your project contains own custom TSLint rules, you will have to re-implement them as ESLint rules to be able to apply them to your code base (see [Custom ESLint rules](./eslint.md#custom-eslint-rules)).

With version 2.0 we introduce a renaming of the two standard PWA themes and change the default theme:

- The previous B2B theme `blue` is now called `b2b` and is used as default theme from now on.
- The previous B2C theme `default` is now called `b2c`.

With this change the according folders and references had to be renamed/moved and need to be adapted in customer projects as well.
In projects where the recommended procedure for using a custom theme has been followed (see [Customization Guide - Start Customization](./customizations.md#start-customization)), minimal migration effort should be required.

We moved the model `SelectOption` from the select.component.ts to the `select-option.model.ts` and adapted all necessary imports.

In the PWA 0.28 we introduced the usage of [Formly](https://formly.dev/) to generate and maintain our forms.
Now we removed the obsolete form components.
If you want to use the obsolete form components in your project nevertheless, skip the commit `remove obsolete form components`.
For more information concerning Formly please refer to our [Formly - Guide](./formly.md)).

The feature toggle 'advancedVariationHandling' has been removed.
Instead the ICM channel preference 'AdvancedVariationHandling' is used to configure it.
You will find this preference as 'List View' in the ICM backoffice under Channel Preferences -> Product Variations.

The ICM channel preference 'basket.maxItemQuantity' is included to validate the product quantity if no specific setting is defined on the product.
You find this preference as 'Maximum Quantity per Product in Cart' under the Application Settings -> Shopping Cart & Checkout.
The default value is 100.

The Intershop PWA 2.0 release includes the Angular 13 update and updates to a lot of other dependencies (NgRx, RxJS, Formly, Swiper).
These dependencies updates require many necessary code adaptions that are included in additional commits.
The following official guides might help to migrate custom code as well:

- https://update.angular.io/?l=3&v=12.0-13.0
- https://ngrx.io/guide/migration/v13
- https://github.com/ngx-formly/ngx-formly/blob/v6.0.0-next.7/UPGRADE-6.0.md
- https://v7.swiperjs.com/migration-guide

To help with the necessary rxjs refactorings, consider using [rxjs-fixers-morph](https://github.com/timdeschryver/rxjs-fixers-morph).
Simply run `npx rxjs-fixers-morph ./tsconfig.json`. | 1 | two days |
| 2.0 | 2.1 | 11 | 14.15.0 LTS | 6.14.8 | The recently viewed products functionality was moved into an extension.
The already existing `recently` feature toggle works as before but the recently viewed component integration changed from `<ish-recently-viewed *ishFeature="'recently'"></ish-recently-viewed>` to `<ish-lazy-recently-viewed></ish-lazy-recently-viewed>`.
This has already been changed for the product detail page and the basket page but needs to be done for any customized usage of the recently viewed component.

The `clean-localizations` functionality was changed so that `keep-localization-pattern` can be defined where they are used and do no longer need to be added directly to the [`clean-up-localizations` script](../../scripts/clean-up-localizations.js).
It might be useful to move custom patterns according to the changes done for the standard code (for more information see [Localization File Clean Up Process](../concepts/localization.md#localization-file-clean-up-process)).

TestBed configuration arrays are sorted again as of 2.1 This means a lot of (small, auto-fixable) changes across the codebase.
Simply run `ng lint --fix` in order to sort your arrays.
If you have a lot of migration changes, you might be required to run it more than once.

With the introduction of personalized REST calls for categories and products, data in the ngrx store runs the risk of not being up-to-date after a login or logout.
To fix this, a new `resetSubStatesOnActionsMeta` meta-reducer was introduced to remove potentially invalid data from the store.
If the removal of previous data from the store is not wanted, this meta reducer should not be used in customized projects.
In addition, a mechanism was introduced to trigger such personalized REST calls after loading the PGID if necessary.
This way of loading personalized data might need to be added to any custom implementations that potentially fetch personalized data.
To get an idea of the necessary mechanism, search for the usage of `useCombinedObservableOnAction` and `personalizationStatusDetermined` in the source code. | 1 | two days |
| 2.1 | 2.2 | 11 | 14.15.0 LTS | 6.14.8 | The PWA 2.2 contains an Angular update to version 13.3.0 and many other dependencies updates.<br/>
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
For other compare components, check the compare-exports.module.ts file. | 1 | two days |
| 2.2 | 2.3 | 11 | 14.15.0 LTS | 6.14.8 | The 'contact us' functionality has been moved into an extension and we have introduced the feature toggle `contactUs` in the `environment.model.ts` that is switched on by default.

The `getFilteredProducts` method has been moved from the `FilterService` to the `ProductsService`, since the `/products` API is used.
Together with this change, the default product attributes for product listings have been externalized and are easily overridable now.

With [#1135](https://github.com/intershop/intershop-pwa/pull/1135), the default model representation used by `NgbDatepicker` is the native ES6 `Date` now.
During this refactoring, the `DateHelper` class has been removed. **This will not concern you if you use `ish-date-picker-field` directly**.
However, if you use `NgbDatepicker` outside of formly, some helpers you might have used are gone.
Please use the underlying functions from `Date`, [`NgbCalendar`](https://ng-bootstrap.github.io/#/components/datepicker/api#NgbCalendar) and [`date-fns`](https://date-fns.org) directly, or create your own `DateHelper`. | 1 | two days |
| 2.3 | 2.4 | 11 | 14.15.0 LTS | 6.14.8 | The PWA 2.4 contains an Angular update to version 13.3.10 and many other dependencies updates.
These updates did not require any updates to the PWA source code.
But it needs to be checked if this is true for your project customizations as well.

We introduced a checkout guard that protects the checkout routes in case no shopping cart is available and navigates back to the empty basket page.

Routes to non-existing CMS content pages now result in a "Page Not Found" error page.

The 'ratings' functionality (components concerning the display of product ratings) has been moved into an extension using the existing feature toggle 'ratings'.

With the display of product reviews the attribute 'numberOfReviews' has been added to the product model, and the number of reviews is displayed behind the product rating stars now instead of the average rating that is already depicted in the stars. | 1 | two days |
| 2.4 | 3.0 | 11 | 14.15.0 LTS | 6.14.8 | With the 2.4.1 Hotfix we introduced a more fixed Node.js version handling to the version used and tested by us.
We set Node.js 16.16.0 and npm 8.11.0 as our application runtime and package management versions.
This is supposed to prevent unexpected build issues in the future but requires manual updating of Node.js to newer versions if tested successfully.
Other Node.js versions might still work but you might get warnings regarding the project's recommended settings.

The Intershop PWA 3.0 release includes a Jest Update to version 28, see also https://jestjs.io/docs/upgrading-to-jest28.
The jest-marbles package has been replaced by jasmine-marbles.

It also contains the Angular 14 update and updates to a lot of other dependencies (NgRx, Typescript).
These updates require some code adaptions, e.g., form classes have been prefixed with _Untyped_ wherever necessary.
The following official guides might help to migrate custom code as well:

- https://update.angular.io/?v=13.0-14.0
- https://ngrx.io/guide/migration/v14
- https://angular.io/guide/typed-forms

Because Angular 14 now uses `yargs` to parse CLI arguments (see [#22778](https://github.com/angular/angular-cli/pull/22778)), schematic options with a `no` prefix are handled differently.
With [#23405](https://github.com/angular/angular-cli/pull/23405), the Angular team has introduced a temporary workaround for this.
In order to reliably maintain compatibility in the future, the `cms` schematic's `noCMSPrefixing` option has been renamed to `cmsPrefixing` with an inverted behavior.

Cypress has been upgraded from version 9 to 10.
We went through the interactive migration to move our spec files from cypress/integration folder to the cypress/e2e folder and updated the config file as well as some scripts.
For more information, see the [Cypress Migration Guide](https://docs.cypress.io/guides/references/migration-guide#Migrating-to-Cypress-version-10-0).

Since the used deferred load library is no longer maintained, it is removed and has been replaced with similar standard browser functionality [`loading="lazy"`](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading#images_and_iframes).
All uses of the `(deferLoad)` directive in custom code need to be replaced.

We removed the unmaintained `angular2-uuid` library in favor of the standard `uuid` library that is already included as an Angular dependency.
In order to match our changes, replace all occurrences of `angular2-uuid` in your custom code (see #1203).

The [pagespeed module](https://www.modpagespeed.com) of NGINX has been removed without replacement.

The [@ngx-translate/http-loader](https://github.com/ngx-translate/core) dependency was removed since we did not use it.
You might need to keep this dependency if you are loading translations differently from the standard Intershop PWA in your customization.

The deprecated `customized-copy` schematic for copying components and replacing all usages was removed.

We introduced a build variable `SSR` that is now used for all checks if the application is running in SSR or browser context.
We no longer use the verbose way of injecting the `PLATFORM_ID` and check it with the methods `isPlatformBrowser` or `isPlatformServer`.
This way still works but it is discouraged by a new ESLint rule that suggests using the new `SSR` variable instead.
So running `npm run lint` will help finding custom code that still relies on the platform checks.

To support, e.g., special characters in e-mail addresses with newer versions of ICM (7.10.38.x), like `+`, double encoding of resource IDs in the REST API calls is necessary.
With the method `encodeResourceID` we provide a central place that implements the fitting resource encoding.
In the PWA this was applied to all user logins in REST API calls.
For project customizations, the usage of the native `encodeURIComponent` functionality should be replaced with `encodeResourceID` for user logins in REST calls as well.

The `footer.content` localization key was replaced for most of its content by a CMS manageable content include `include.footer.content.pagelet2-Include` that is available from ICM 7.10.38.9-LTS.

For better Search Engine Optimization the route formate and route handling for products, categories, and content pages has been reworked.
All these routes now contain hierarchies and have different ID markers.
For categories it was changed from `cat` to `ctg` and for products from `sku`to `prd`.
This way, it is intended to have less conflicts and limitations with potential category/product IDs, e.g., 'cats' or 'skunks'.

To improve the support of large baskets we update the ngrx store immediately after adding, updating, and deleting basket items now.
Therefore, we had to change the return values of the corresponding basket service functions as well as the payload of the success actions.
We also limited the number of displayed line items in the mini basket and introduced a paging bar on the basket page to speed up the rendering of these components. | 1 | two days |
| 3.0 | 3.1 | 11 | 14.15.0 LTS | 6.14.8 | The SSR environment variable `ICM_IDENTITY_PROVIDER` will be removed in the next major release (PWA 4.0).
Use variable `IDENTITY_PROVIDER` to select the provider to be used instead.
Keep this in mind before deploying or starting the Intershop PWA in server-side rendering mode.

The default value of the input parameter ['queryParamsHandling'](https://angular.io/api/router/QueryParamsHandling) has been changed from `'merge'` to `''` for the components `product-name.component` and `product-image.component`.
This has been done to prevent an unintentional application of filters for product variation master links if the product detail link does not originate from a product listing context (product list page, search result page).

To prevent deprecation warnings, we removed the unnecessary `~` from all 3rd party SCSS imports (see https://webpack.js.org/loaders/sass-loader/#resolving-import-at-rules - "Using ~ is deprecated and can be removed from your code (we recommend it)").
This should be done for additional imports in the customizations as well.

The validator `equalToControl` did not work properly.
For that reason we removed it.
Use the validator `equalTo` instead.
For more information, see the method description in the [`special-validators.ts`](https://github.com/intershop/intershop-pwa/blob/3.0.0/src/app/shared/forms/validators/special-validators.ts#L82-L87).

The "Product Image Not Available" PNG image `not_available.png` is removed and replaced by an SVG image `not-available.svg` which does not include a text inside the image anymore to avoid localization issues.
The file references are updated accordingly, the product image component is updated to use the correct image attributes, a localized alternative text is added, and the product and image mapper files are updated to provide the correct data.
In case the current PNG image file and the handling is customized in a project, you have to ensure to keep the project changes. | 1 | two days |
| 3.1 | 3.2 | 11 | 14.15.0 LTS | 6.14.8 | A styling adaption was made to the application shell to expand it to the full page height, so the footer now always stays at the bottom.
Together with that an inline style of the `main-container` was moved to the global styling definition.

Formly has been upgraded from version 5 to 6.
For more information, see the [Formly Upgrade Guide](https://github.com/ngx-formly/ngx-formly/blob/main/UPGRADE-6.0.md).
We still use deprecated form properties like `templateOptions` and `expressionProperties` for compatibility reasons but we are going to replace them in the next major release.

The two small black triangle images `active_catalog.png` (header: when hovering a catalog) and `budget-bar-indicator.png` (my account: budget bar) are removed and replaced by CSS styling.
The image for an empty basket `empty-cart.png` is removed and replaced with CSS styling.
The sprite image `product_sprite.png` is removed and replaced with localized text for "New", "Sale", and "Top" with the according CSS styling.

After entering a desired delivery date on the checkout shipping page and after submitting the order, the desired delivery date will be saved at all basket items if necessary.
In case of large baskets (> 20 items) this might cause long response times.
You can keep the existing behavior by modifying the `updateBasketItemsDesiredDeliveryDate()` method of the basket service to always return an empty array without doing anything.

The `ProductsService` was changed to use `extended=true` REST calls for product details and variations to fetch variation attributes with additional `attributeType` and `metaData` information that can be used to control the rendering of different variation select types.
The added `VariationAttributeMapper` maps the additional information in a backwards compatible way.
To handle the different variation select rendering types, the existing `ProductVariationSelectComponent` now contains the logic to select the fitting variation select rendering component.
The rendering and behavior of the existing `ProductVariationSelectComponent` as a standard select box was moved to the new `ProductVariationSelectDefaultComponent`.
A `ProductVariationSelectSwatchComponent` for colorCode and swatchImage variation select rendering and a `ProductVariationSelectEnhancedComponent` for a select box rendering with color codes or swatch images and a mobile optimization were added.

The user authentication process has changed.
User authentication tokens are requested from the ICM server using the `/token` REST endpoint now.
Regarding this, the logout action triggers a service which revokes the currently available access token on the ICM backend.
If the logout was successful, all personalized information is removed from the ngrx store.
Please use `logoutUser({ revokeToken: false })` from the account facade or dispatch `logoutUserSuccess` instead of the `logoutUser` action to use the old behavior. | 1 | two days |
| 3.2 | 3.3 | 11 | 14.15.0 LTS | 6.14.8 | To improve the accessibility of the PWA in regards to more elements being tab focusable, a lot of `[routerLink]="[]"` where added to links that previously did not have a link reference.
Also some `(keydown.enter)` event bindings with `tabindex="0"` were added to ensure a better interactivity with the keyboard only.
If the according commits lead to problems, they could be skipped and resolved later by fixing the accessibility linting issues manually.
More information regarding accessibility in the PWA and the used ESLint rules can be found in the [Accessibility Guide](./accessibility.md). | 1 | two days |
| 3.3 | 4.0 | 11 | 14.15.0 LTS | 6.14.8 | The Intershop PWA now uses Node.js 18.15.0 LTS with the corresponding npm version 9.5.0 and the `"lockfileVersion": 3,`.
For migrating the `package-lock.json`, it is always advised to use the `package-lock.json` from the Intershop PWA and then run `npm install` to update it with the additional custom dependencies from the customer project's `package.json`.

The project was updated to work with Angular 15.
This includes the removal of the Browserslist configuration and an updated TypeScript compiler `target` and `lib` to `ES2022` (for browser support requirements that differ from the Angular 15 standard configuration, see the [configuring browser compatibility](https://angular.io/guide/build#configuring-browser-compatibility) guide and the [TypeScript configuration](https://angular.io/guide/typescript-configuration) reference).
Adaptions of the Schematics configurations and tests were also necessary.
In addition, all other dependencies were updated as well and resulted in necessary Stylelint and Jest test adaptions.

The placeholder for theme-specific assets and styles has been changed from `placeholder` to `theme_placeholder`.
If this is used in any customization, update all paths which are using the old theme placeholder, e.g., `src/styles/themes/placeholder` to `src/styles/themes/theme_placeholder`.

The injection token `LOCAL_TRANSLATIONS` was introduced to use local translation files within the custom [ICM translation loader](https://github.com/intershop/intershop-pwa/blob/4.0.0/src/app/core/utils/translate/icm-translate-loader.ts).
A factory function is provided in the [`internationalization.module.ts`](https://github.com/intershop/intershop-pwa/blob/4.0.0/src/app/core/internationalization.module.ts) to decide which json file with translation keys should be used for a given language.

```typescript
  providers: [
    ...
    {
      provide: LOCAL_TRANSLATIONS,
      useValue: {
        useFactory: (lang: string) => {
          switch (lang) {
            case 'en_US':
              return import('../../assets/i18n/en_US.json');
            case 'fr_FR':
              return import('../../assets/i18n/fr_FR.json');
            case 'de_DE':
              return import('../../assets/i18n/de_DE.json');
          }
        },
      },
    },
  ],
```

Please adapt the `useFactory()` function to return all imported local translation files depending on the `lang` parameter.

With Angular 15 class-based route guards are deprecated in favor of functional guards.
Thus, we removed the guard classes and replaced them by functions.
For the `canActivate/canChildActivate` methods, only change the class name into the function name by lowercasing the first letter, e.g.,

```typescript
{
  path: 'organization-management',
  ...
  canActivate: [AuthGuard],
  canActivateChild: [AuthGuard],
}
```

will become

```typescript
{
  path: 'organization-management',
  ...
  canActivate: [authGuard],
  canActivateChild: [authGuard],
},
```

For more information about functional guards, see this [blog article](https://blog.angular.io/advancements-in-the-angular-router-5d69ec4c032).

With the [Prettier update to version 2.8](https://prettier.io/blog/2022/11/23/2.8.0.html#angular) the format of pipes in HTML files changed slightly.

After updating [Jest to version 29](https://jestjs.io/docs/upgrading-to-jest29#snapshot-format) the default snapshot formatting changed.
Run `npm run test -- -u` to update your test snapshots.

The account navigation has been reworked to support navigation grouping (used in `b2b` theme, see [`account-navigation.items.ts`](https://github.com/intershop/intershop-pwa/blob/4.0.0/src/app/pages/account/account-navigation/account-navigation.items.ts)).
For better maintainability and brand-specific overriding, the account navigation items were externalized in an extra file `account-navigation.items.ts` used by the `account-navigation.component.ts`.
With this rework also the navigation items data structure was changed from a key value object to a simpler `NavigationItem` array.
With this data structure accessing the data was changed for the key access from `item.key` to `item.routerLink`, or for the value example from `item.value.localizationKey` to `item.localizationKey`.
To migrate to this new account navigation item handling, any account navigation customization needs to be adapted accordingly.

The deprecated SSR environment variable `ICM_IDENTITY_PROVIDER` was completely removed.
Use the variable `IDENTITY_PROVIDER` instead to select the identity provider to be used if it is not the default `ICM`.
We removed the default `identityProvider` configuration from `environment.model.ts`, so only the hardcoded fallback from `configuration.effects.ts` works as fallback.

The deprecated properties `templateOptions` and `expressionProperties` have been removed from the `FormlyFieldConfiguration` object.
Current projects **must** use the new properties for all formly field configurations.
You **must** adapt html templates, too, when using the deprecated properties in there.

To replace deprecated formly field properties, you can execute the new `formly-migrate` schematic.
Please run the following command for each configured Angular project (e.g., 'intershop-pwa'):

```console
  ng g formly-migrate --project=${ANGULAR_PROJECT}
```

> **NOTE:** Not all scenarios where a deprecated property could be found are taken into consideration for the `formly-migrate` schematic. Please check and adapt your code manually for additional changes. For further information, see the [formly migration guide](https://formly.dev/docs/guide/migration/).

The templates of `account-order-template-detail-page.component.ts`, `quote-line-item-list.component.ts`, `quoting-basket-line-items.component.ts`, and `account-wishlist-detail-page.component.ts` have been updated to ensure correct DOM element updates for `ngFor` loop changes.
A [trackBy function](https://angular.io/api/core/TrackByFunction) will be used now.

Obsolete functionality that is no longer needed with the current state of the Intershop PWA was removed from the project source code:

- Removed outdated `kubernetes-deployment` schematic that could be used to create Kubernetes charts. Use the official [Intershop PWA Helm Chart repository](https://github.com/intershop/helm-charts/tree/main/charts/pwa) instead.
- Removed unused `azure-pipeline` schematic that could be used to create an Azure Pipeline template based on the generated Kubernetes charts for DevOps.
- Removed migration scripts that were used for pre PWA 1.0 migration support.
- Removed obsolete TODO comments and related logic that handled, for example, wrong/odd/old REST API quirks.

We recommend to use the Action Group Creator to create store actions now.
Therefore, the corresponding store schematic for the action creation has been adapted.

We added some helper methods to improve the use of dependency injection.
Use the method `createEnvironmentInjectionToken` now to define new injection keys for environment variables in the `injection-keys.ts`.
If you want to inject a token, use the methods `injectSingle` and `injectMultiple` to secure the type safety of your injected variables (except for Angular core tokens, which are forced to a type).
There is a new linting rule `useTypeSafeInjectionTokenRule` that enforces the usage of these methods.
For more information, see the [Configuration Concept](../concepts/configuration.md#angular-cli-environments).

We introduced the product notifications feature as a new extension which can be enabled with the feature toggle `productNotifications`. | 1 | two days |
| 4.0 | 4.1 | 11 | 14.15.0 LTS | 6.14.8 | The Intershop PWA now uses Node.js 18.16.0 LTS with the corresponding npm version 9.5.1 to resolve an issue with Azure Docker deployments (see #1416).

As a leftover adaption regarding the switch from deprecated class-based route guards in favor of functional guards the `addGlobalGuard` function was adapted to work with functional guards.
If the `addGlobalGuard` function is used for customizations, make sure it now works as expected.

The input parameter `id` of the component `ish-product-quantity` caused issues with duplicate IDs within the page html.
Therefore, it was renamed to `elementId`.
If the input parameter 'id' of this component has already been used, it has to be renamed accordingly.

The `ishIntersectionObserver` returns all three `IntersectionStatus` change events: `Visible`, `Pending`, and `NotVisible` as well now.
The custom project code needs to be adapted if it does not filter the events where it is used (e.g., `if (event === 'Visible')`).

The two standard themes `b2b` and `b2c` where refactored in such a way that the `b2c` theme could be changed into a [configurable theme](./themes.md#configurable-theme) that uses CSS custom properties (CSS variables).
Since SCSS color calculations do not work with CSS custom properties (they need real values instead of `var(--corporate-primary)`), SCSS functions like `darken()` and `lighten()` were removed from the standard Intershop PWA SCSS styling.
Existing projects that do not want to use a configurable theme do not need to apply these changes to their custom styling.

To use the new [configurable theme](./themes.md#configurable-theme) feature, the feature toggle `extraConfiguration` needs to be enabled.

A new `TokenService` is introduced to be only responsible for fetching token data from the ICM.
However, all necessary adaptions for the identity providers and the `fetchToken()` method of the UserService are removed in order to be completely independent of `TokenService`.
If your identity providers should use the `OAuthService` to handle the authentication, please make sure to instantiate a new `OAuthService` entity within the identity provider.
The `getOAuthServiceInstance()` static method from the `InstanceCreators` class can be used for that.
Furthermore, the handling of the anonymous user token has been changed.
It will only be fetched when an anonymous user intends to create a basket.

We added an Address Doctor integration as a new extension which can be enabled with the feature toggle `addressDoctor` and [additional configuration](./address-doctor.md). | 1 | two days |
| 4.1 | 4.2 | 11 | 14.15.0 LTS | 6.14.8 | The basket attribute 'orderReferenceId' is now saved as native attribute 'externalOrderReference' at the basket, but it still exists at the basket and can be displayed further on if needed.

A better handling for cookie `SameSite` and `secure` settings was implemented with new defaults to `SameSite=Strict` and `secure`.
This can still be overridden when calling the `cookies.services` `put` method with explicitly set values.
Now the `secure` setting is always set to `true` if in `https` mode.
You can prevent this by explicitly setting it to `false`.
If the PWA is run with `http` (should only be in development environments), `secure` is not set.
Additionally, if the PWA is run in an iframe, all cookies are set with `SameSite=None` (e.g., for punchout or Design View).
Be aware that some browsers no longer accept cookies with `SameSite=None` without `secure`.
Before, by default no `SameSite` was set so browsers treated it as `SameSite=Lax`.
This needs to be set explicitly now if it is really intended.
For migrating, check whether the calls of the `cookies.service` `put` method need to be adapted.

The user's language selection is saved as a cookie (`preferredLocale`) now and restored after the PWA has loaded.
This functionality can be enabled/disabled with the feature toggle `saveLanguageSelection`. | 1 | two days |