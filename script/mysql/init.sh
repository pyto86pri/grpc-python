#!/bin/bash

mysql -u user -ppassword test <<-EOSQL
    DROP TABLE IF EXISTS `users`;

    CREATE TABLE IF NOT EXISTS `users`
    (
        `id`     VARCHAR(20) NOT NULL,
        `name`   VARCHAR(20) NOT NULL,
            PRIMARY KEY (`id`)
    )
EOSQL