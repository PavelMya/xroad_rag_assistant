### 2.25 UI_USERS

UI user name with its last used locale. Maps possible user interface (UI) user names with locales so that when UI user is logged in next time, the locale it has been used is remembered. If a user with no assigned locale logs in, the first available locale is selected to this user. Later user can change its locale in the user interface.

The record is created when the user is logged in the user interface for the first time. The record is modified when the user logged in changes its locale in the user interface. The record is never deleted.