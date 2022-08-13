CREATE_USERS_QUEUE = '''CREATE TABLE IF NOT EXISTS users
                                (
                                ID              INT       PRIMARY KEY       NOT NULL,
                                IS_REGISTERED   BOOLEAN                     NOT NULL,
                                AREA            TEXT                        NOT NULL,
                                POSITION        TEXT                        NOT NULL,
                                EXP             TEXT                        NOT NULL,
                                LANG            TEXT                        NOT NULL,
                                CITY            TEXT                        NOT NULL,
                                SALARY          TEXT                        NOT NULL
                                ); '''

CREATE_VACANCIES_QUEUE = '''CREATE TABLE IF NOT EXISTS vacancies
                                (
                                ID             SMALLSERIAL   PRIMARY KEY    NOT NULL,
                                TITLE          TEXT                         NOT NULL,
                                INFO           TEXT                         NOT NULL,
                                LANG           TEXT                                 ,
                                AREA           TEXT                         NOT NULL,
                                POSITION       TEXT                         NOT NULL,
                                EXP            TEXT                         NOT NULL,
                                COMPANY_NAME   TEXT                                 ,
                                COUNTRY        TEXT                         NOT NULL,
                                CITY           TEXT                         NOT NULL,
                                REMOTE         TEXT                                 ,
                                SALARY         SMALLINT                             ,
                                LINK           TEXT                         NOT NULL,
                                IS_ACTUAL      BOOL                         NOT NULL
                                ); '''  # noqa
