#!/usr/bin/env bash

mongo localhost:27017
use starwars
if ( db.getCollectionNames().length=== 0) {db.createCollection('planets');}