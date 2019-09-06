# Tietokannan create table -lauseet



### Event
```
CREATE TABLE event (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        description VARCHAR(144), 
        minimum INTEGER NOT NULL, 
        creator_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(creator_id) REFERENCES account (id)
);
```


### Account
```
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);
```

### userEvent (liitostaulu)
```
CREATE TABLE userevent (
        account_id INTEGER NOT NULL, 
        event_id INTEGER NOT NULL, 
        PRIMARY KEY (account_id, event_id), 
        FOREIGN KEY(account_id) REFERENCES account (id), 
        FOREIGN KEY(event_id) REFERENCES event (id)
);
```
