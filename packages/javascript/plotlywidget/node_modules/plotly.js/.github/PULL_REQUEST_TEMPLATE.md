Thanks for your interest in plotly.js!

### Translations:

- Make a PR directly to the main repository
- Please @ mention a few other speakers of this language who can help review your translations.
- If you've omitted any keys from [dist/translation_keys.txt](https://github.com/plotly/plotly.js/blob/master/dist/translation-keys.txt) - which means they will fall back on the US English text - just make a short comment about why in the PR description: the English text works fine in your language, or you would like someone else to help translating those, or whatever the reason.
- You should only update files in `lib/locales/`, not those in `dist/`

### Features, Bug fixes, and others:

Developers are strongly encouraged to first make a PR to their own plotly.js fork and ask one of the maintainers to review the modifications there. Once the pull request is deemed satisfactory, the developer will be asked to make a pull request to the main plotly.js repo and may be asked to squash some commits before doing so.

Before opening a pull request, developer should: 

- `git rebase` their local branch off the latest `master`,
- make sure to **not** `git add` the `dist/` folder (the `dist/` is updated only on version bumps),
- make sure to commit changes to the `package-lock.json` file (if any),
- write an overview of what the PR attempts to do,
- select the _Allow edits from maintainers_ option (see this [article](https://help.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) for more details).

Note that it is forbidden to force push (i.e. `git push -f`) to remote branches associated with opened pull requests. Force pushes make it hard for maintainers to keep track of updates. Therefore, if required, please `git merge master` into your PR branch instead of `git rebase master`.
