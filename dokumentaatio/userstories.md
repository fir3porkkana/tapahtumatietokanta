## User storyt

* Tapahtuman järjestäjänä tahdon nähdä, ketkä ovat tulossa paikalle. Tapahtumaan liitetyt käyttäjät saadaan selville seuraavanlaisella kyselyllä:
    ```
    SELECT account.id, account.name FROM account
                    JOIN userevent ON userevent.account_id = account.id
                    WHERE userevent.event_id = [tarkasteltavan tapahtuman id - event_id]
                    
* Osallistujana haluan nähdä, missä, milloin tapahtuma järjestetään ja mikä sen aihe on. Tapahtuman luoja/organisoija selvitetään suorittamalla kysely
    ```
    SELECT account.name FROM account
                    WHERE account.id = [tarkasteltavan tapahtuman luojan id - creator_id]
